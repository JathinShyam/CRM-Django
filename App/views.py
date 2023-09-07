from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm, SendEmailForm
from .models import Record
import csv
from django.core.mail import EmailMessage
from django.conf import settings
import os


def home(request):
    records = Record.objects.all()
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
        return render(request, 'home.html', {'records': records})


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
        # Look Up Records
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record': customer_record})
    else:
        messages.success(request, "You Must Be Logged In To View That Page...")
        return redirect('home')


def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Record Deleted Successfully...")
        return redirect('home')
    else:
        messages.success(request, "You Must Be Logged In To Do That...")
        return redirect('home')


def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "Record Added...")
                return redirect('home')
        return render(request, 'add_record.html', {'form': form})
    else:
        messages.success(request, "You Must Be Logged In...")
        return redirect('home')


def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record Has Been Updated!")
            return redirect('home')
        return render(request, 'update_record.html', {'form': form})
    else:
        messages.success(request, "You Must Be Logged In...")
        return redirect('home')


# def send_email(request, pk):
#     pass


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

                # Loop through each row and save it to the 'Record' model
                for row in csv_reader:
                    new_record = Record(
                        first_name=row['first_name'],
                        last_name=row['last_name'],
                        email=row['email'],
                        phone=row['phone'],
                        address=row['address'],
                        city=row['city'],
                        state=row['state'],
                        pincode=row['pincode']
                    )
                    new_record.save()

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
