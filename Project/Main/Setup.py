#Importing Required Modules

import random as r
import mysql.connector as ms
from Vars import *

#Code Blocks for Customisation in Company or a Preset

def Setup():

    global  Departments, Jobs
    
    print('''
        Choose All The Departments You Desire:
        (A) Sales 
        (B) Marketing
        (C) HR
        (D) Finance
        (E) IT
        (F) Operations
        (G) Customer Service
        (H) R&D
        (I) Legal
        (J) Administration
        (K) Supply Chain
        (L) Quality Assurance
        (M) Public Relations
        (N) Product Management
        (O) Engineering
        (P) Design
        (Q) Health and Safety
        (R) Training and Development
        (S) Compliance
    ''')
    Deps=input('Enter Letter of Every Department you Require: ')
    
    Departments = []
    Jobs = {}
    Deps = [i for i in Deps]

    if 'A' in Deps:

        N=1
        Sales=[]
        print('SALES')
        print('There is 1 necessary job for Sales Supervisor')
        Sales.append('Sales Supervisor')
        n=int(input('Enter no of Sales Managers desired: '))
        N+=n
        for i in range(n):
            Sales.append('Sales Manager')
        n=int(input('Enter no of Account Executives desired: '))
        N+=n
        for i in range(n):
            Sales.append('Account Executive')
        n=int(input('Enter no of Sales Representatives desired: '))
        N+=n
        for i in range(n):
            Sales.append('Sales Representative')
        n=int(input('Enter no of Sales Coordinators desired: '))
        N+=n
        for i in range(n):
            Sales.append('Sales Coordinator')
        for i in range(N):
            Departments.append('Sales')
        Jobs['Sales'] = Sales

    if 'B' in Deps:

        N=1
        Marketing=[]
        print('MARKETING')
        print('There is 1 necessary job for Marketing Supervisor')
        Marketing.append('Marketing Supervisor')
        n=int(input('Enter no of Marketing Managers desired: '))
        N+=n
        for i in range(n):
            Marketing.append('Marketing Manager')
        n=int(input('Enter no of Marketing Coordinators desired: '))
        N+=n
        for i in range(n):
            Marketing.append('Marketing Coordinator')
        n=int(input('Enter no of Marketing Analysts desired: '))
        N+=n
        for i in range(n):
            Marketing.append('Marketing Analyst')
        n=int(input('Enter no of Digital Marketing Specialists desired: '))
        N+=n
        for i in range(n):
            Marketing.append('Digital Marketing Specialist')
        for i in range(N):
            Departments.append('Marketing')
        Jobs['Marketing']=Marketing

    if 'C' in Deps:

        N=1
        HR=[]
        print('HUMAN RESOURCE')
        print('There is 1 necessary job for HR Supervisor')
        HR.append('HR Supervisor')
        n=int(input('Enter no of HR Managers desired: '))
        N+=n
        for i in range(n):
            HR.append('HR Manager')
        n=int(input('Enter no of HR Coordinators desired: '))
        N+=n
        for i in range(n):
            HR.append('HR Coordinator')
        n=int(input('Enter no of HR Recruiters desired: '))
        N+=n
        for i in range(n):
            HR.append('HR Recruiter')
        n=int(input('Enter no of HR Generalists desired: '))
        N+=n
        for i in range(n):
            HR.append('HR Generalist')
        for i in range(N):
            Departments.append('HR')
        Jobs['HR'] = HR

    if 'D' in Deps:

        N=1
        Finance=[]
        print('FINANCE')
        print('There is 1 necessary job for Finance Supervisor')
        Finance.append('Finance Supervisor')
        n=int(input('Enter no of Finance Managers desired: '))
        N+=n
        for i in range(n):
            Finance.append('Finance Manager')
        n=int(input('Enter no of Financial Analysts desired: '))
        N+=n
        for i in range(n):
            Finance.append('Financial Analyst')
        n=int(input('Enter no of Accountants desired: '))
        N+=n
        for i in range(n):
            Finance.append('Accountant')
        n=int(input('Enter no of Budget Analysts desired: '))
        N+=n
        for i in range(n):
            Finance.append('Budget Analyst')
        for i in range(N):
            Departments.append('Finance')
        Jobs['Finance'] = Finance

    if 'E' in Deps:

        N=1
        IT=[]
        print('INFORMATION TECHNOLOGY')
        print('There is 1 necessary job for IT Supervisor')
        IT.append('IT Supervisor')
        n=int(input('Enter no of IT Managers desired: '))
        N+=n
        for i in range(n):
            IT.append('IT Manager')
        n=int(input('Enter no of Software Engineers desired: '))
        N+=n
        for i in range(n):
            IT.append('Software Engineer')
        n=int(input('Enter no of Network Administrators desired: '))
        N+=n
        for i in range(n):
            IT.append('Network Administrator')
        n=int(input('Enter no of Database Administrators desired: '))
        N+=n
        for i in range(n):
            IT.append('Database Administrator')
        for i in range(N):
            Departments.append('IT')
        Jobs['IT'] = IT

    if 'F' in Deps:

        N=1
        Operations=[]
        print('OPERATIONS')
        print('There is 1 necessary job for Operations Supervisor')
        Operations.append('Operations Supervisor')
        n=int(input('Enter no of Operations Managers desired: '))
        N+=n
        for i in range(n):
            Operations.append('Operations Manager')
        n=int(input('Enter no of Operations Coordinators desired: '))
        N+=n
        for i in range(n):
            Operations.append('Operations Coordinator')
        n=int(input('Enter no of Process Improvement Analysts desired: '))
        N+=n
        for i in range(n):
            Operations.append('Process Improvement Analyst')
        n=int(input('Enter no of Quality Assurance Specialists desired: '))
        N+=n
        for i in range(n):
            Operations.append('Quality Assurance Specialist')
        for i in range(N):
            Departments.append('Operations')
        Jobs['Operations'] = Operations

    if 'G' in Deps:

        N=1
        Customer_Service=[]
        print('CUSTOMER SERVICE')
        print('There is 1 necessary job for Customer Service Supervisor')
        Customer_Service.append('Customer Service Supervisor')
        n=int(input('Enter no of Customer Service Managers desired: '))
        N+=n
        for i in range(n):
            Customer_Service.append('Customer Service Manager')
        n=int(input('Enter no of Customer Support Specialists desired: '))
        N+=n
        for i in range(n):
            Customer_Service.append('Customer Support Specialist')
        n=int(input('Enter no of Call Center Representatives desired: '))
        N+=n
        for i in range(n):
            Customer_Service.append('Call Center Representative')
        n=int(input('Enter no of Customer Experience Analysts desired: '))
        N+=n
        for i in range(n):
            Customer_Service.append('Customer Experience Analyst')
        for i in range(N):
            Departments.append('Customer Service')
        Jobs['Customer Service'] = Customer_Service

    if 'H' in Deps:
        
        N=1
        R_and_D=[]
        print('RESOURCE & DEVELOPMENT')
        print('There is 1 necessary job for R&D Supervisor')
        R_and_D.append('R&D Supervisor')
        n=int(input('Enter no of R&D Managers desired: '))
        N+=n
        for i in range(n):
            R_and_D.append('R&D Manager')
        n=int(input('Enter no of Research Scientists desired: '))
        N+=n
        for i in range(n):
            R_and_D.append('Research Scientist')
        n=int(input('Enter no of Product Development Engineers desired: '))
        N+=n
        for i in range(n):
            R_and_D.append('Product Development Engineer')
        n=int(input('Enter no of Lab Technicians desired: '))
        N+=n
        for i in range(n):
            R_and_D.append('Lab Technician')
        for i in range(N):
            Departments.append('R&D')
        Jobs['R&D'] = R_and_D

    if 'I' in Deps:

        N=1
        Legal=[]
        print('LEGAL')
        print('There is 1 necessary job for Legal Supervisor')
        Legal.append('Legal Supervisor')
        n=int(input('Enter no of Legal Counsels desired: '))
        N+=n
        for i in range(n):
            Legal.append('Legal Counsel')
        n=int(input('Enter no of Corporate Lawyers desired: '))
        N+=n
        for i in range(n):
            Legal.append('Corporate Lawyer')
        n=int(input('Enter no of Paralegals desired: '))
        N+=n
        for i in range(n):
            Legal.append('Paralegal')
        n=int(input('Enter no of Legal Assistants desired: '))
        N+=n
        for i in range(n):
            Legal.append('Legal Assistant')
        for i in range(N):
            Departments.append('Legal')
        Jobs['Legal'] = Legal

    if 'J' in Deps:

        N=1
        Administration=[]
        print('ADMINISTRATION')
        print('There is 1 necessary job for Administrative Supervisor')
        Administration.append('Administrative Supervisor')
        n=int(input('Enter no of Administrative Managers desired: '))
        N+=n
        for i in range(n):
            Administration.append('Administrative Manager')
        n=int(input('Enter no of Office Coordinators desired: '))
        N+=n
        for i in range(n):
            Administration.append('Office Coordinator')
        n=int(input('Enter no of Administrative Assistants desired: '))
        N+=n
        for i in range(n):
            Administration.append('Administrative Assistant')
        n=int(input('Enter no of Office Clerks desired: '))
        N+=n
        for i in range(n):
            Administration.append('Office Clerk')
        for i in range(N):
            Departments.append('Administration')
        Jobs['Administration'] = Administration

    if 'K' in Deps:

        N=1
        SupplyChain=[]
        print('SUPPLY CHAIN')
        print('There is 1 necessary job for Supply Chain Supervisor')
        SupplyChain.append('Supply Chain Supervisor')
        n=int(input('Enter no of Supply Chain Managers desired: '))
        N+=n
        for i in range(n):
            SupplyChain.append('Supply Chain Manager')
        n=int(input('Enter no of Procurement Specialists desired: '))
        N+=n
        for i in range(n):
            SupplyChain.append('Procurement Specialist')
        n=int(input('Enter no of Logistics Coordinators desired: '))
        N+=n
        for i in range(n):
            SupplyChain.append('Logistics Coordinator')
        n=int(input('Enter no of Inventory Analysts desired: '))
        N+=n
        for i in range(n):
            SupplyChain.append('Inventory Analyst')
        for i in range(N):
            Departments.append('Supply Chain')
        Jobs['Supply Chain'] = SupplyChain

    if 'L' in Deps:

        N=1
        QualityAssurance=[]
        print('QUALITY ASSURANCE')
        print('There is 1 necessary job for QA Supervisor')
        QualityAssurance.append('QA Supervisor')
        n=int(input('Enter no of QA Managers desired: '))
        N+=n
        for i in range(n):
            QualityAssurance.append('QA Manager')
        n=int(input('Enter no of Quality Control Inspectors desired: '))
        N+=n
        for i in range(n):
            QualityAssurance.append('Quality Control Inspector')
        n=int(input('Enter no of QA Engineers desired: '))
        N+=n
        for i in range(n):
            QualityAssurance.append('QA Engineer')
        n=int(input('Enter no of Compliance Auditors desired: '))
        N+=n
        for i in range(n):
            QualityAssurance.append('Compliance Auditor')
        for i in range(N):
            Departments.append('Quality Assurance')
        Jobs['Quality Assurance'] = QualityAssurance

    if 'M' in Deps:

        N=1
        PublicRelations=[]
        print('PUBLIC RELATIONS')
        print('There is 1 necessary job for PR Supervisor')
        PublicRelations.append('PR Supervisor')
        n=int(input('Enter no of PR Managers desired: '))
        N+=n
        for i in range(n):
            PublicRelations.append('PR Manager')
        n=int(input('Enter no of PR Specialists desired: '))
        N+=n
        for i in range(n):
            PublicRelations.append('PR Specialist')
        n=int(input('Enter no of Media Relations Coordinators desired: '))
        N+=n
        for i in range(n):
            PublicRelations.append('Media Relations Coordinator')
        n=int(input('Enter no of Communications Strategists desired: '))
        N+=n
        for i in range(n):
            PublicRelations.append('Communications Strategist')
        for i in range(N):
            Departments.append('Public Relations')
        Jobs['Public Relations'] = PublicRelations

    if 'N' in Deps:

        N=1
        ProductManagement=[]
        print('PRODUCT MANAGEMENT')
        print('There is 1 necessary job for Product Supervisor')
        ProductManagement.append('Product Supervisor')
        n=int(input('Enter no of Product Managers desired: '))
        N+=n
        for i in range(n):
            ProductManagement.append('Product Manager')
        n=int(input('Enter no of Product Owners desired: '))
        N+=n
        for i in range(n):
            ProductManagement.append('Product Owner')
        n=int(input('Enter no of Product Marketing Managers desired: '))
        N+=n
        for i in range(n):
            ProductManagement.append('Product Marketing Manager')
        n=int(input('Enter no of Product Analysts desired: '))
        N+=n
        for i in range(n):
            ProductManagement.append('Product Analyst')
        for i in range(N):
            Departments.append('Product Management')
        Jobs['Product Management'] = ProductManagement

    if 'O' in Deps:

        N=1
        Engineering=[]
        print('ENGINEERING')
        print('There is 1 necessary job for Engineering Supervisor')
        Engineering.append('Engineering Supervisor')
        n=int(input('Enter no of Engineer Managers desired: '))
        N+=n
        for i in range(n):
            Engineering.append('Engineering Manager')
        n=int(input('Enter no of Mechanical Engineers desired: '))
        N+=n
        for i in range(n):
            Engineering.append('Mechanical Engineer')
        n=int(input('Enter no of Electrical Engineers desired: '))
        N+=n
        for i in range(n):
            Engineering.append('Electrical Engineer')
        n=int(input('Enter no of Civil Engineers desired: '))
        N+=n
        for i in range(n):
            Engineering.append('Civil Engineer')
        for i in range(N):
            Departments.append('Engineering')
        Jobs['Engineering'] = Engineering

    if 'P' in Deps:

        N=1
        Design=[]
        print('DESIGN')
        print('There is 1 necessary job for Design Supervisor')
        Design.append('Design Supervisor')
        n=int(input('Enter no of Design Managers desired: '))
        N+=n
        for i in range(n):
            Design.append('Design Manager')
        n=int(input('Enter no of Graphic Designers desired: '))
        N+=n
        for i in range(n):
            Design.append('Graphic Designer')
        n=int(input('Enter no of UX/UI Designers desired: '))
        N+=n
        for i in range(n):
            Design.append('UX/UI Designer')
        n=int(input('Enter no of Industrial Designers desired: '))
        N+=n
        for i in range(n):
            Design.append('Industrial Designer')
        for i in range(N):
            Departments.append('Design')
        Jobs['Design'] = Design

    if 'Q' in Deps:

        N=1
        Health_Safety=[]
        print('HEALTH & SAFETY')
        print('There is 1 necessary job for H&S Supervisor')
        Health_Safety.append('H&S Supervisor')
        n=int(input('Enter no of H&S Managers desired: '))
        N+=n
        for i in range(n):
            Health_Safety.append('H&S Manager')
        n=int(input('Enter no of Safety Coordinators desired: '))
        N+=n
        for i in range(n):
            Health_Safety.append('Safety Coordinator')
        n=int(input('Enter no of Occupational Health Specialists desired: '))
        N+=n
        for i in range(n):
            Health_Safety.append('Occupational Health Specialist')
        n=int(input('Enter no of Environmental Health Officers desired: '))
        N+=n
        for i in range(n):
            Health_Safety.append('Environmental Health Officer')
        for i in range(N):
            Departments.append('Health and Safety')
        Jobs['Health and Safety'] = Health_Safety

    if 'R' in Deps:

        N=1
        Training_Development=[]
        print('TRAINING & DEVELOPMENT')
        print('There is 1 necessary job for Training Supervisor')
        Training_Development.append('Training Supervisor')
        n=int(input('Enter no of Training Managers desired: '))
        N+=n
        for i in range(n):
            Training_Development.append('Training Manager')
        n=int(input('Enter no of Learning and Development Specialists desired: '))
        N+=n
        for i in range(n):
            Training_Development.append('Learning and Development Specialist')
        n=int(input('Enter no of Training Coordinators desired: '))
        N+=n
        for i in range(n):
            Training_Development.append('Training Coordinator')
        n=int(input('Enter no of Instructional Designers desired: '))
        N+=n
        for i in range(n):
            Training_Development.append('Instructional Designer')
        for i in range(N):
            Departments.append('Training and Development')
        Jobs['Training and Development'] = Training_Development

    if 'S' in Deps:

        N=1
        Compliance=[]
        print('COMPLIANCE')
        print('There is 1 necessary job for Compliance Supervisor')
        Compliance.append('Compliance Supervisor')
        n=int(input('Enter no of Compliance Managers desired: '))
        N+=n
        for i in range(n):
            Compliance.append('Compliance Manager')
        n=int(input('Enter no of Compliance Analysts desired: '))
        N+=n
        for i in range(n):
            Compliance.append('Compliance Analyst')
        n=int(input('Enter no of Regulatory Affairs Specialists desired: '))
        N+=n
        for i in range(n):
            Compliance.append('Regulatory Affairs Specialist')
        n=int(input('Enter no of Ethics and Compliance Officers desired: '))
        N+=n
        for i in range(n):
            Compliance.append('Ethics and Compliance Officer')
        for i in range(N):
            Departments.append('Compliance')
        Jobs['Compliance'] = Compliance

    return [Jobs,Departments]
    
def PreSet():
    global Jobs,Departments
    
    Deps='ABCDEFGHIJKLMNOPQRS'
    N =11
    Departments = []
    Jobs = {}

    if 'A' in Deps:

        Sales=[]
        Sales.append('Sales Supervisor')
        for i in range(1):
            Sales.append('Sales Manager')
        for i in range(2):
            Sales.append('Account Executive')
        for i in range(3):
            Sales.append('Sales Representative')
        for i in range(4):
            Sales.append('Sales Coordinator')
        for i in range(N):
            Departments.append('Sales')
        Jobs['Sales'] = Sales

    if 'B' in Deps:

        Marketing=[]
        Marketing.append('Marketing Supervisor')
        for i in range(1):
            Marketing.append('Marketing Manager')
        for i in range(2):
            Marketing.append('Marketing Coordinator')
        for i in range(3):
            Marketing.append('Marketing Analyst')
        for i in range(4):
            Marketing.append('Digital Marketing Specialist')
        for i in range(N):
            Departments.append('Marketing')
        Jobs['Marketing']=Marketing

    if 'C' in Deps:

        HR=[]
        HR.append('HR Supervisor')
        for i in range(1):
            HR.append('HR Manager')
        for i in range(2):
            HR.append('HR Coordinator')
        for i in range(3):
            HR.append('HR Recruiter')
        for i in range(4):
            HR.append('HR Generalist')
        for i in range(N):
            Departments.append('HR')
        Jobs['HR'] = HR

    if 'D' in Deps:

        Finance=[]
        Finance.append('Finance Supervisor')
        for i in range(1):
            Finance.append('Finance Manager')
        for i in range(2):
            Finance.append('Financial Analyst')
        for i in range(3):
            Finance.append('Accountant')
        for i in range(4):
            Finance.append('Budget Analyst')
        for i in range(N):
            Departments.append('Finance')
        Jobs['Finance'] = Finance

    if 'E' in Deps:

        IT=[]
        IT.append('IT Supervisor')
        for i in range(1):
            IT.append('IT Manager')
        for i in range(2):
            IT.append('Software Engineer')
        for i in range(3):
            IT.append('Network Administrator')
        for i in range(4):
            IT.append('Database Administrator')
        for i in range(N):
            Departments.append('IT')
        Jobs['IT'] = IT

    if 'F' in Deps:

        Operations=[]
        Operations.append('Operations Supervisor')
        for i in range(1):
            Operations.append('Operations Manager')
        for i in range(2):
            Operations.append('Operations Coordinator')
        for i in range(3):
            Operations.append('Process Improvement Analyst')
        for i in range(4):
            Operations.append('Quality Assurance Specialist')
        for i in range(N):
            Departments.append('Operations')
        Jobs['Operations'] = Operations

    if 'G' in Deps:

        Customer_Service=[]
        Customer_Service.append('Customer Service Supervisor')
        for i in range(1):
            Customer_Service.append('Customer Service Manager')
        for i in range(2):
            Customer_Service.append('Customer Support Specialist')
        for i in range(3):
            Customer_Service.append('Call Center Representative')
        for i in range(4):
            Customer_Service.append('Customer Experience Analyst')
        for i in range(N):
            Departments.append('Customer Service')
        Jobs['Customer Service'] = Customer_Service

    if 'H' in Deps:
        
        R_and_D=[]
        R_and_D.append('R&D Supervisor')
        for i in range(1):
            R_and_D.append('R&D Manager')
        for i in range(2):
            R_and_D.append('Research Scientist')
        for i in range(3):
            R_and_D.append('Product Development Engineer')
        for i in range(4):
            R_and_D.append('Lab Technician')
        for i in range(N):
            Departments.append('R&D')
        Jobs['R&D'] = R_and_D

    if 'I' in Deps:

        Legal=[]
        Legal.append('Legal Supervisor')
        for i in range(1):
            Legal.append('Legal Counsel')
        for i in range(2):
            Legal.append('Corporate Lawyer')
        for i in range(3):
            Legal.append('Paralegal')
        for i in range(4):
            Legal.append('Legal Assistant')
        for i in range(N):
            Departments.append('Legal')
        Jobs['Legal'] = Legal

    if 'J' in Deps:

        Administration=[]
        Administration.append('Administrative Supervisor')
        for i in range(1):
            Administration.append('Administrative Manager')
        for i in range(2):
            Administration.append('Office Coordinator')
        for i in range(3):
            Administration.append('Administrative Assistant')
        for i in range(4):
            Administration.append('Office Clerk')
        for i in range(N):
            Departments.append('Administration')
        Jobs['Administration'] = Administration

    if 'K' in Deps:

        SupplyChain=[]
        SupplyChain.append('Supply Chain Supervisor')
        for i in range(1):
            SupplyChain.append('Supply Chain Manager')
        for i in range(2):
            SupplyChain.append('Procurement Specialist')
        for i in range(3):
            SupplyChain.append('Logistics Coordinator')
        for i in range(4):
            SupplyChain.append('Inventory Analyst')
        for i in range(N):
            Departments.append('Supply Chain')
        Jobs['Supply Chain'] = SupplyChain

    if 'L' in Deps:

        QualityAssurance=[]
        QualityAssurance.append('QA Supervisor')
        for i in range(1):
            QualityAssurance.append('QA Manager')
        for i in range(2):
            QualityAssurance.append('Quality Control Inspector')
        for i in range(3):
            QualityAssurance.append('QA Engineer')
        for i in range(4):
            QualityAssurance.append('Compliance Auditor')
        for i in range(N):
            Departments.append('Quality Assurance')
        Jobs['Quality Assurance'] = QualityAssurance

    if 'M' in Deps:

        PublicRelations=[]
        PublicRelations.append('PR Supervisor')
        for i in range(1):
            PublicRelations.append('PR Manager')
        for i in range(2):
            PublicRelations.append('PR Specialist')
        for i in range(3):
            PublicRelations.append('Media Relations Coordinator')
        for i in range(4):
            PublicRelations.append('Communications Strategist')
        for i in range(N):
            Departments.append('Public Relations')
        Jobs['Public Relations'] = PublicRelations

    if 'N' in Deps:

        ProductManagement=[]
        ProductManagement.append('Product Supervisor')
        for i in range(1):
            ProductManagement.append('Product Manager')
        for i in range(2):
            ProductManagement.append('Product Owner')
        for i in range(3):
            ProductManagement.append('Product Marketing Manager')
        for i in range(4):
            ProductManagement.append('Product Analyst')
        for i in range(N):
            Departments.append('Product Management')
        Jobs['Product Management'] = ProductManagement

    if 'O' in Deps:

        Engineering=[]
        Engineering.append('Engineering Supervisor')
        for i in range(1):
            Engineering.append('Engineering Manager')
        for i in range(2):
            Engineering.append('Mechanical Engineer')
        for i in range(3):
            Engineering.append('Electrical Engineer')
        for i in range(4):
            Engineering.append('Civil Engineer')
        for i in range(N):
            Departments.append('Engineering')
        Jobs['Engineering'] = Engineering

    if 'P' in Deps:

        Design=[]
        Design.append('Design Supervisor')
        for i in range(1):
            Design.append('Design Manager')
        for i in range(2):
            Design.append('Graphic Designer')
        for i in range(3):
            Design.append('UX/UI Designer')
        for i in range(4):
            Design.append('Industrial Designer')
        for i in range(N):
            Departments.append('Design')
        Jobs['Design'] = Design

    if 'Q' in Deps:

        Health_Safety=[]
        Health_Safety.append('H&S Supervisor')
        for i in range(1):
            Health_Safety.append('H&S Manager')
        for i in range(2):
            Health_Safety.append('Safety Coordinator')
        for i in range(3):
            Health_Safety.append('Occupational Health Specialist')
        for i in range(4):
            Health_Safety.append('Environmental Health Officer')
        for i in range(N):
            Departments.append('Health and Safety')
        Jobs['Health and Safety'] = Health_Safety

    if 'R' in Deps:

        Training_Development=[]
        Training_Development.append('Training Supervisor')
        for i in range(1):
            Training_Development.append('Training Manager')
        for i in range(2):
            Training_Development.append('Learning and Development Specialist')
        for i in range(3):
            Training_Development.append('Training Coordinator')
        for i in range(4):
            Training_Development.append('Instructional Designer')
        for i in range(N):
            Departments.append('Training and Development')
        Jobs['Training and Development'] = Training_Development

    if 'S' in Deps:

        Compliance=[]
        Compliance.append('Compliance Supervisor')
        for i in range(1):
            Compliance.append('Compliance Manager')
        for i in range(2):
            Compliance.append('Compliance Analyst')
        for i in range(3):
            Compliance.append('Regulatory Affairs Specialist')
        for i in range(4):
            Compliance.append('Ethics and Compliance Officer')
        for i in range(N):
            Departments.append('Compliance')
        Jobs['Compliance'] = Compliance
    
    return [Jobs,Departments]

#Code Blocks to generate 1-time sample record for Employee Table

def gen_dob():
    n1=r.randint(1960,2001)
    n2=r.randint(1,12)
    n3=r.randint(1,28)
    if n2<10:
        if n3<10:
            D = str(n1) + '-' + '0' + str(n2) + '-' + '0' + str(n3)
        else:
            D = str(n1) + '-' + '0' + str(n2) + '-' + str(n3)
    else:
        if n3<10:
            D = str(n1) + '-' + str(n2) + '-' + '0' + str(n3)
        else:
            D = str(n1) + '-' + str(n2) + '-' + str(n3)
    return D

def female():
    fn = r.choice(first_names_female)
    chance = r.randint(1,3)
    if chance != 1:
        mn = 'NULL'
    else:
        mn = r.choice(middle_names_female)
    ln = r.choice(last_names)
    dob = gen_dob()
    dep = r.choice(Departments)
    Departments.remove(dep)
    job = r.choice(Jobs[dep])
    Jobs[dep].remove(job)
    rec = [fn,mn,ln,dob,dep,job]    
    return rec

def male():
    fn = r.choice(first_names_male)
    chance = r.randint(1,3)
    if chance != 1:
        mn = 'NULL'
    else:
        mn = r.choice(middle_names_male)
    ln = r.choice(last_names)
    dob = gen_dob()
    dep = r.choice(Departments)
    Departments.remove(dep)
    job = r.choice(Jobs[dep])
    Jobs[dep].remove(job)
    rec = [fn,mn,ln,dob,dep,job]
    return rec

def empsample():
    g=r.choice(Gender)
    if g=='F':
        rec=female()
    elif g=='M':
        rec=male()
    else:
        chance=r.randint(1,2)
        if chance!=2:
            rec=female()
        else:
            rec=male()
    rec.append(g)
    Samples.append(rec)
    return rec

#Code Blocks to generate 1-time sample data for Userkeys Table records

def gen_passkey():
    while True:
        passkey = ''.join(r.choice(Characters) for i in range(5))
        if passkey not in PassKeys:
            PassKeys.append(passkey)
            break
    return passkey

def gen_contact():
    while True:
        contact= ''.join(r.choice(Digits) for i in range(10))
        if int(contact) > 999999999:
            if contact not in Contacts:
                Contacts.append(contact)
                break
    return contact

#Code Block to generate 1-time sample record for Details Table

def detsample():
    hno= str(r.choice(Digits)) + str(r.choice(Digits)) + str(r.choice(Digits))
    sttp= r.choice(street_types)
    stnm= r.choice(street_names)
    addr= hno + '-' + sttp + '-' + stnm
    st=r.choice(us_states)
    nrec=r.choice(us_states_cities[st])
    ct=nrec[0]
    zp=nrec[1]
    sample = [addr,ct,st,zp]
    return sample

#Code Blocks to Fill in Records in Tables Procedurally

def fillemployee(n):
    con=ms.connect(host='localhost',user='root',password=sql_password,database=sql_db)
    cur=con.cursor()
    for i in range(n):
        rec=empsample()
        fn = rec[0]
        mn = rec[1]
        ln = rec[2]
        dob = rec[3]
        dep = rec[4]
        job = rec[5]
        g = rec[6]
        cur.execute(f"insert into Employee (First_Name, Middle_Name, Last_Name, DOB, Gender, Department, Job) values('{fn}','{mn}','{ln}','{dob}','{g}','{dep}','{job}')")
        con.commit()
    con.close()

def filluserkeys(n):
    con=ms.connect(host='localhost',user='root',password=sql_password,database=sql_db)
    cur=con.cursor()
    cur.execute('select * from Employee')
    db=cur.fetchall()
    for i in range(n):
        while True:
            if db[i][2] == 'NULL':
                un = db[i][1].upper() + r.choice(Digits) + db[i][3].lower() + r.choice(Digits) + r.choice(Digits)
            else:
                un = db[i][1].upper() + r.choice(Digits) + db[i][3].lower() + r.choice(Digits) + db[i][2]
            if un not in Userlist:
                Userlist.append(un)
                break
        pk=gen_passkey()
        mail = db[i][1].lower() + str(db[i][0]) + f"@{company_name.lower()}.com"
        cn=gen_contact()
        cur.execute(f"insert into UserKeys (UserName, PassKey, Mail, Contact) values('{un}','{pk}','{mail}','{cn}')")
        con.commit()
    con.close()

def filldetails(n):
    con=ms.connect(host='localhost',user='root',password=sql_password,database=sql_db)
    cur=con.cursor()
    for i in range(n):
        rec = detsample()
        addr = rec[0]
        ct = rec[1]
        st = rec[2]
        zp = rec[3]
        cur.execute(f"insert into Details (Address, City, State, Zipcode) values('{addr}','{ct}','{st}','{zp}')")
        con.commit()
    con.close()

#Code Blocks to Check for existence of required database and Tables and Create if required 

def chkDatabase():
    try:
        con=ms.connect(host='localhost',user='root',password=sql_password,database=sql_db)
    except:
        con=ms.connect(host='localhost',user='root',password=sql_password)
        cur=con.cursor()
        cur.execute(f"create database {sql_db}")
        con.commit()
        con.close()

def chkEmployee(n):
    con=ms.connect(host='localhost',user='root',password=sql_password,database=sql_db)
    cur=con.cursor()
    try:
        cur.execute("select * from Employee")
    except:
        cur.execute("""CREATE TABLE Employee (
        Employee_ID INT AUTO_INCREMENT PRIMARY KEY,
        First_Name VARCHAR(255),
        Middle_Name VARCHAR(255),
        Last_Name VARCHAR(255),
        DOB DATE,
        Gender ENUM('F', 'M', 'Other'),
        Department ENUM('Sales', 'Marketing', 'HR', 'Finance', 'IT', 'Operations', 'Customer Service', 'R&D', 'Legal', 'Administration', 'Supply Chain', 'Quality Assurance', 'Public Relations', 'Product Management', 'Engineering', 'Design', 'Health and Safety', 'Training and Development', 'Compliance'),
        Job VARCHAR(255)
        )""")
        con.commit()
        con.close()
        fillemployee(n)

def chkUserkeys(n):   
    con=ms.connect(host='localhost',user='root',password=sql_password,database=sql_db)
    cur=con.cursor() 
    try:
        cur.execute("select * from Userkeys")
    except:
        cur.execute("""CREATE TABLE UserKeys (
        Employee_ID INT AUTO_INCREMENT PRIMARY KEY,
        UserName VARCHAR(255),
        PassKey VARCHAR(255),
        Mail VARCHAR(255),
        Contact BIGINT,
        UNIQUE (UserName,PassKey,Mail,Contact)
        )""")
        con.commit()
        con.close()
        filluserkeys(n)

def chkDetails(n):
    con=ms.connect(host='localhost',user='root',password=sql_password,database=sql_db)
    cur=con.cursor()
    try:
        cur.execute("select * from Details")
    except:
        cur.execute('''CREATE TABLE Details (
        Employee_ID INT AUTO_INCREMENT PRIMARY KEY,
        Address VARCHAR(255),
        City VARCHAR(255),
        State VARCHAR(255),
        Zipcode VARCHAR(255)
        );''')
        con.commit()
        con.close()
        filldetails(n)

def chkMessages():
    con=ms.connect(host='localhost',user='root',password=sql_password,database=sql_db)
    cur=con.cursor()
    try:
        cur.execute("select * from Messages")
    except:
        cur.execute("""CREATE TABLE Messages (
        Sender VARCHAR(255),
        Reciever VARCHAR(255),
        Time TIMESTAMP,
        Message LONGTEXT
        );""")
        con.commit()
        con.close()

def chkUpdates():
    con=ms.connect(host='localhost',user='root',password=sql_password,database=sql_db)
    cur=con.cursor()
    try:
        cur.execute("select * from Updates")
    except:
        cur.execute("""CREATE TABLE Updates (
        Update_Query VARCHAR(255)
        );""")
        con.commit()
        con.close()

#Main Code to Setup

choice=int(input('''
                 (1) To Use a Preset Company
                 (2) To Generate a Custom Company
                 (3) Delete Prior Company
                 Enter Choice:'''))
if choice == 3:
    try:
        con=ms.connect(host='localhost',user='root',password=sql_password,database=sql_db)
        cur=con.cursor()
        cur.execute(f'drop database {sql_db}')
    except:
        pass
else:
    if choice == 1:
            A=PreSet()
    elif choice == 2:
            A=Setup()
    Jobs=A[0]
    Departments=A[1]
    n=len(Departments)
    chkDatabase()
    chkEmployee(n)
    chkUserkeys(n)
    chkDetails(n)
    chkMessages()
    chkUpdates()