from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddCustomerForm, SendEmailForm, SearchForm, CustomerQueryForm, AssignEmployeeForm
from .models import *
import csv
from django.core.mail import EmailMessage
from django.conf import settings
import os
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import get_user_model
import random

def home(request):
    # customers = Customer.objects.all()

    # Retrieve all customer records
    customer_query = Customer.objects.all()

    # Create a Paginator instance with 15 records per page
    paginator = Paginator(customer_query, 15)

    # Get the current page number from the request's GET parameters
    page = request.GET.get('page')

    try:
        customers = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver the first page.
        customers = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g., 9999), deliver the last page of results.
        customers = paginator.page(paginator.num_pages)


    # Check to see if logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You Have Been Logged In!")
            return redirect('home')
        else:
            messages.success(request, "There Was An Error Logging In, Please Try Again...")
            return redirect('home')
    else:
        return render(request, 'home.html', {'customers': customers})


def logout_user(request):
    logout(request)
    messages.success(request, "You Have Been Logged Out...")
    return redirect('home')


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You Have Successfully Registered! Welcome!")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})

    return render(request, 'register.html', {'form': form})


def customer_record(request, pk):
    if request.user.is_authenticated:
        # Look Up Customers
        customer_record = Customer.objects.get(id=pk)
        return render(request, 'customer.html', {'customer_record': customer_record})
    else:
        messages.success(request, "You Must Be Logged In To View That Page...")
        return redirect('home')


def delete_customer(request, pk):
    if request.user.is_authenticated:
        delete_it = Customer.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Customer Deleted Successfully...")
        return redirect('home')
    else:
        messages.success(request, "You Must Be Logged In To Do That...")
        return redirect('home')


def add_customer(request):
    form = AddCustomerForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_customer = form.save()
                messages.success(request, "Customer Added...")
                return redirect('home')
        return render(request, 'add_customer.html', {'form': form})
    else:
        messages.success(request, "You Must Be Logged In...")
        return redirect('home')


def update_customer(request, pk):
    if request.user.is_authenticated:
        current_customer = Customer.objects.get(id=pk)
        form = AddCustomerForm(request.POST or None, instance=current_customer)
        if form.is_valid():
            form.save()
            messages.success(request, "Customer Has Been Updated!")
            return redirect('home')
        return render(request, 'update_customer.html', {'form': form})
    else:
        messages.success(request, "You Must Be Logged In...")
        return redirect('home')


def import_csv(request):
    if request.user.is_authenticated:
        if request.method == "POST" and request.FILES['csv_file']:
            csv_file = request.FILES['csv_file']

            if not csv_file.name.endswith('.csv'):
                messages.error(request, 'Please upload a CSV file.')
                return redirect('import_csv')  # Redirect back to the import page with an error message

            try:
                # Read the CSV file
                decoded_file = csv_file.read().decode('utf-8').splitlines()
                csv_reader = csv.DictReader(decoded_file)

                # Loop through each row and save it to the 'Customer' model
                for row in csv_reader:
                    new_customer = Customer(
                        first_name=row['first_name'],
                        last_name=row['last_name'],
                        email=row['email'],
                        phone=row['phone'],
                        address=row['address'],
                        city=row['city'],
                        state=row['state'],
                        pincode=row['pincode']
                    )
                    new_customer.save()

                messages.success(request, 'CSV file uploaded and data saved successfully.')
                return redirect('import_csv')  # Redirect back to the import page with a success message

            except Exception as e:
                messages.error(request, f'Error processing CSV file: {e}')
                return redirect('import_csv')  # Redirect back to the import page with an error message

        return render(request, 'import_csv.html')

    else:
        messages.success(request, "You Must Be Logged In To Do That...")
        return redirect('home')


def send_email(request):
    if request.method == "POST":
        form = SendEmailForm(request.POST, request.FILES)

        if form.is_valid():
            subject = form.cleaned_data['subject']
            body = form.cleaned_data['body']
            recipient_emails = form.cleaned_data['recipient_email']
            attachment = request.FILES.get('attachment')

            try:
                # Split the input string of email addresses into a list
                recipient_email_list = [email.strip() for email in recipient_emails.split(',')]

                # Create an EmailMessage object for each recipient
                for recipient_email in recipient_email_list:
                    email = EmailMessage(subject, body, settings.DEFAULT_FROM_EMAIL, [recipient_email])

                    # Attach a file if provided
                    if attachment:
                        email.attach(attachment.name, attachment.read(), attachment.content_type)

                    # Send the email
                    email.send()

                messages.success(request, 'Email(s) sent successfully.')
                return redirect('send_email')  # Redirect back to the email form with a success message

            except Exception as e:
                messages.error(request, f'Error sending email: {e}')
                return redirect('send_email')  # Redirect back to the email form with an error message

    else:
        form = SendEmailForm()

    return render(request, 'send_email.html', {'form': form})



def search_results(request):
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():

            search_query = request.GET.get('search_query', '')
            # Use filter() to find customers where 'first_name' starts with the search query
            customers = Customer.objects.filter(Q(first_name__startswith=search_query) | 
                                            Q(last_name__startswith=search_query))
        else:
            customers = Customer.objects.all()
    else:
        customers = Customer.objects.all()
        form = SearchForm()

    context = {
        'customers': customers,
    }

    return render(request, 'search_results.html', context)


def assignEmployee(query:str) -> str:
    if query == "Account Management" or query == "General Inquiries":
        return "Customer Support Representative"
    elif query == "Product Inquiries":
        return "Product Specialist"
    elif query == "Order Status and Tracking":
        return "Logistics Coordinator"
    elif query == "Complaints" or query == "Feedback and Suggestions":
        return "Lead"
    elif query == "Returns and Refunds" or query == "Technical Support":
        return "IT Support Technician"
    elif query == "Payment Issues":
        return "Financial Analyst"
    elif query == "Offers and Promotions":
        return "Marketing Coordinator"
    

def submit_query(request):
    if request.method == 'POST':
        form = CustomerQueryForm(request.POST)
        if form.is_valid():
            # Create a new CustomerQuery instance
            # customer_query = form.save(commit=False) # Create but don't save yet
            customer_query = CustomerQuery()
            customer_query.customer = form.cleaned_data['customer']
            customer_query.query = form.cleaned_data['query']
            customer_query.query_text = form.cleaned_data['query_text']
            employee_type = assignEmployee(customer_query.query)
            employees = Employee.objects.filter(designation=employee_type)
            if employees:
                customer_query.employee_assigned = random.choice(employees)
            customer_query.resolved = False  # Set initial query status
            customer_query.save()  # Save the query
            messages.success(request, "Query submitted successfully!")
            return redirect('submit_query')  # Redirect to the query submission page
    else:
        form = CustomerQueryForm()

    return render(request, 'submit_query.html', {'form': form})


@login_required
@user_passes_test(lambda user: user.is_superuser or not hasattr(user, 'Employee'))
def view_queries(request):
    queries = CustomerQuery.objects.all()

    return render(request, 'view_queries.html', {'queries': queries})


def assign_employee(request):
    employees = Employee.objects.all()
    if request.method == 'POST':
        form = AssignEmployeeForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            employee = form.cleaned_data['employee']
            query.employee_assigned = employee
            query.save()
            messages.success(request, "Query assigned to the Employee successfully!")
    else:
        # Fetch the list of leads to display in the assignment form
        form = AssignEmployeeForm()
        
    return render(request, 'assign_employee.html', {'form': form, 'employees': employees})
