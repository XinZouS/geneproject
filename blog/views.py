# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from .models import Company, Advisors
from django.db.models import Q



def home(request):
	content = {
		# 'companys': Company.objects.all()
		'companys': Company.objects.order_by("Name")[:10] # get first 10 rows 
	}
	return render(request, 'blog/home.html', content)


def company_full(request):
	cols = ["Name", "CUSIP", "SecId", "FundId", "Master FundId", "PerformanceId", "Ticker", "Oldest Share Class", "Advisor", "Firm Name", "Branding Name", "Branding Name ID", "Inception Date", "Global Broad Category Group", "Global Category", "US Category Group", "Morningstar Category", "Morningstar Category Id", "Morningstar Category Start Date", "Morningstar Institutional Category", "Morningstar Rating Overall", "Morningstar Rating 3 Yr", "Morningstar Rating 5 Yr", "Morningstar Rating 10 Yr", "Equity Style Box (Long)", "Equity Style Box (Short)", "Fixed Inc Style Box (Long)", "Subadvisor", "Subadvisor Fee Ratio", "Team Managed", "Manager History", "Manager Name", "Manager Tenure (Average)", "Manager Tenure (Longest)", "Primary Prospectus Benchmark", "Primary Prospectus Benchmark Id", "Primary Prospectus Benchmark Inception Date", "Secondary Prospectus Benchmark", "Net Assets - Share Class Base Currency", "Net Assets Date", "Fund Size Base Currency", "Fund Size Date", "# of Bond Holdings (Long)", "# of Bond Holdings (Short)", "# of Holdings (Long)", "# of Other Holdings (Long)", "# of Other Holdings (Short)", "# of Stock Holdings (Long)", "# of Stock Holdings (Short)", "% Asset in Top 10 Holdings", "Holding of an Investment", "Latest % Asset in Top 10 Holdings", "Latest % Asset in Top 10 Holdings Date", "12 Mo Yield", "12 Mo Yield Date", "SEC Yield", "SEC Yield Date", "Latest Dividend Base Currency", "Latest Dividend Date", "Latest Dividend NAV Base Currency", "Portfolio Date", "Virtual Class", "Management Fee", "Semi-Annual Report Net Expense Ratio", "Semi-Annual Report Net Expense Ratio Date", "Annual Report Ongoing Charge", "Annual Report Ongoing Charge Date", "Prospectus Net Expense Ratio", "Prospectus Gross Expense Ratio", "Prospectus Objective", "12b-1 Fee", "Turnover Ratio %", "Turnover Ratio % Date", "Cash % (Net)", "Asset Alloc Bond % (Net)", "Asset Alloc Cash % (Net)", "Asset Alloc Equity % (Net)", "Asset Alloc Non-US Bond % (Net)", "Asset Alloc Non-US Equity % (Net)", "Asset Alloc Other % (Net)", "Asset Alloc US Bond % (Net)", "Asset Alloc US Equity % (Net)", "Asset Backed % (Net)", "Asset Alloc Bond % (Long)", "Asset Alloc Cash % (Long)", "Asset Alloc Equity % (Long)", "Asset Alloc Non-US Bond % (Long)", "Asset Alloc Non-US Equity % (Long)", "Asset Alloc Other % (Long)", "Asset Alloc US Bond % (Long)", "Asset Alloc US Equity % (Long)", "In-House FOF", "Leveraged Fund", "Feeder Fund", "Master Fund", "Master Fund Name", "Master FundId", "Sharia Compliant", "Ethical Issue Strategy Focus", "Model Portfolio Fund", "Available For 529 Only", "Available For Retirement Plan", "Available In Insurance Product", "Tax Managed", "Contrarian", "Brokerage Availability", "Enhanced Index", "Index Fund", "Fund of Funds", "Socially Conscious", "Non Diversified", "Closed to All Inv", "Closed to All Investors Date", "Closed to New Inv", "Closed to New Investors Date", "Accounting Fee", "Administrator Fee", "Advisor Fee", "Auditor Fee", "Custodian Fee", "Distribution Fee", "Insurance Fee", "Legal Fee", "Organization Fee", "Other Fee", "Performance Fee", "Professional Fee", "Registration Fee", "Shareholder Reporting Fee", "Transfer Agency Fee", "Domicile", "Base Currency", "Obsolete Date", "Obsolete Type", "Discount (Current)", "Share Class Type", "Asset Alloc Bond % (Long Rescaled)", "Asset Alloc Bond % (Long)", "Asset Alloc Cash % (Long Rescaled)", "Asset Alloc Conv Bond % (Long Rescaled)", "Asset Alloc Equity % (Long Rescaled)", "Asset Alloc Non-US Bond % (Long Rescaled)", "Asset Alloc Non-US Equity % (Long Rescaled)", "Asset Alloc Other % (Long Rescaled)", "Asset Alloc Pref Stock % (Long Rescaled)", "Asset Alloc US Bond % (Long Rescaled)", "Asset Alloc US Equity % (Long Rescaled)"]
	content = {
		# 'companys': Company.objects.all()
		'companys': Company.objects.order_by("Name")[:50], # get first n rows 
		'colnames': cols
	}
	return render(request, 'blog/company_full.html', content)


def company_13rows(request):
	cols = ["Name", "CUSIP", "SecId", "FundId", "Master FundId", "PerformanceId", "Ticker", "Oldest Share Class", "Advisor", "Firm Name", "Branding Name", "Branding Name ID", "Inception Date"]
	content = {
		'companys': Company.objects.order_by("Name")[:50], # get first n rows 
		'colnames': cols
	}
	return render(request, 'blog/company_13rows.html', content)


def advisor_table(request, advisorid=0):
	cols = ["Name", "CUSIP", "SecId", "FundId"]

	if advisorid == 0:
		cmpinfo = Company.objects.order_by("Name")
	else:
		cmpinfo = Company.objects.filter(AdvisorID_id=advisorid).order_by("Name")

	# plan A: use Company to filter out all Advisors:
	# advs = Company.objects.values('Advisor').exclude(Advisor__isnull=True).order_by("Advisor").distinct()
	# plan B: use new table Advisor to provide info: 
	advs = Advisors.objects.all()
	
	advsNames = list(map(lambda x: x.Name.encode("utf-8"), advs))

	advsObj = Advisors.objects.filter(id=advisorid)
	selected = {'Name':'Select an Advisor'} if len(advsObj)==0 else advsObj[0]

	content = {
		'companys': cmpinfo, # get first n rows 
		'colnames': cols,
		'advisors': advs,
		'advisorNames': advsNames,
		'selected': selected,
	}
	return render(request, 'blog/advisor_table.html', content)


def about(request):
	return render(request, 'blog/about.html')






