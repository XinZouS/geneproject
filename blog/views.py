# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Company, Advisors, MSCats, MSSubAdvs, Funds, Shares

import time


@login_required
def home(request):
	content = {
		# 'companys': Company.objects.all()
		'companys': Company.objects.order_by("Name")[:10] # get first 10 rows 
	}
	return render(request, 'blog/home.html', content)


@login_required
def company_full(request):
	cols = ["Name", "CUSIP", "SecId", "FundId", "Master FundId", "PerformanceId", "Ticker", "Oldest Share Class", "Advisor", "Firm Name", "Branding Name", "Branding Name ID", "Inception Date", "Global Broad Category Group", "Global Category", "US Category Group", "Morningstar Category", "Morningstar Category Id", "Morningstar Category Start Date", "Morningstar Institutional Category", "Morningstar Rating Overall", "Morningstar Rating 3 Yr", "Morningstar Rating 5 Yr", "Morningstar Rating 10 Yr", "Equity Style Box (Long)", "Equity Style Box (Short)", "Fixed Inc Style Box (Long)", "Subadvisor", "Subadvisor Fee Ratio", "Team Managed", "Manager History", "Manager Name", "Manager Tenure (Average)", "Manager Tenure (Longest)", "Primary Prospectus Benchmark", "Primary Prospectus Benchmark Id", "Primary Prospectus Benchmark Inception Date", "Secondary Prospectus Benchmark", "Net Assets - Share Class Base Currency", "Net Assets Date", "Fund Size Base Currency", "Fund Size Date", "# of Bond Holdings (Long)", "# of Bond Holdings (Short)", "# of Holdings (Long)", "# of Other Holdings (Long)", "# of Other Holdings (Short)", "# of Stock Holdings (Long)", "# of Stock Holdings (Short)", "% Asset in Top 10 Holdings", "Holding of an Investment", "Latest % Asset in Top 10 Holdings", "Latest % Asset in Top 10 Holdings Date", "12 Mo Yield", "12 Mo Yield Date", "SEC Yield", "SEC Yield Date", "Latest Dividend Base Currency", "Latest Dividend Date", "Latest Dividend NAV Base Currency", "Portfolio Date", "Virtual Class", "Management Fee", "Semi-Annual Report Net Expense Ratio", "Semi-Annual Report Net Expense Ratio Date", "Annual Report Ongoing Charge", "Annual Report Ongoing Charge Date", "Prospectus Net Expense Ratio", "Prospectus Gross Expense Ratio", "Prospectus Objective", "12b-1 Fee", "Turnover Ratio %", "Turnover Ratio % Date", "Cash % (Net)", "Asset Alloc Bond % (Net)", "Asset Alloc Cash % (Net)", "Asset Alloc Equity % (Net)", "Asset Alloc Non-US Bond % (Net)", "Asset Alloc Non-US Equity % (Net)", "Asset Alloc Other % (Net)", "Asset Alloc US Bond % (Net)", "Asset Alloc US Equity % (Net)", "Asset Backed % (Net)", "Asset Alloc Bond % (Long)", "Asset Alloc Cash % (Long)", "Asset Alloc Equity % (Long)", "Asset Alloc Non-US Bond % (Long)", "Asset Alloc Non-US Equity % (Long)", "Asset Alloc Other % (Long)", "Asset Alloc US Bond % (Long)", "Asset Alloc US Equity % (Long)", "In-House FOF", "Leveraged Fund", "Feeder Fund", "Master Fund", "Master Fund Name", "Master FundId", "Sharia Compliant", "Ethical Issue Strategy Focus", "Model Portfolio Fund", "Available For 529 Only", "Available For Retirement Plan", "Available In Insurance Product", "Tax Managed", "Contrarian", "Brokerage Availability", "Enhanced Index", "Index Fund", "Fund of Funds", "Socially Conscious", "Non Diversified", "Closed to All Inv", "Closed to All Investors Date", "Closed to New Inv", "Closed to New Investors Date", "Accounting Fee", "Administrator Fee", "Advisor Fee", "Auditor Fee", "Custodian Fee", "Distribution Fee", "Insurance Fee", "Legal Fee", "Organization Fee", "Other Fee", "Performance Fee", "Professional Fee", "Registration Fee", "Shareholder Reporting Fee", "Transfer Agency Fee", "Domicile", "Base Currency", "Obsolete Date", "Obsolete Type", "Discount (Current)", "Share Class Type", "Asset Alloc Bond % (Long Rescaled)", "Asset Alloc Bond % (Long)", "Asset Alloc Cash % (Long Rescaled)", "Asset Alloc Conv Bond % (Long Rescaled)", "Asset Alloc Equity % (Long Rescaled)", "Asset Alloc Non-US Bond % (Long Rescaled)", "Asset Alloc Non-US Equity % (Long Rescaled)", "Asset Alloc Other % (Long Rescaled)", "Asset Alloc Pref Stock % (Long Rescaled)", "Asset Alloc US Bond % (Long Rescaled)", "Asset Alloc US Equity % (Long Rescaled)"]
	content = {
		# 'companys': Company.objects.all()
		'companys': Company.objects.order_by("Name")[:50], # get first n rows 
		'colnames': cols
	}
	return render(request, 'blog/company_full.html', content)


@login_required
def company_13rows(request):
	cols = ["Name", "CUSIP", "SecId", "FundId", "Master FundId", "PerformanceId", "Ticker", "Oldest Share Class", "Advisor", "Firm Name", "Branding Name", "Branding Name ID", "Inception Date"]
	content = {
		'companys': Company.objects.order_by("Name")[:50], # get first n rows 
		'colnames': cols
	}
	return render(request, 'blog/company_13rows.html', content)


@login_required
def advisor_table(request):
	cols = ["No.", "Name", "CUSIP", "SecId", "FundId", "Advisor", "MSCat", "MSSubAdv"]
	companyInfo = []
	sharesAndFundsCols = ["No.", "Advisor", "FundId", "MSCat", "TR_YTD", "TR_1Y", "TR_2Y", "TR_3Y", "TR_4Y", "TR_5Y", "TR_10Y", "TR_15Y", "TR_2017", "TR_2016", "TR_2015", "TR_2014", "TR_2013", "TR_2012", "TR_2011", "TR_2010", "TR_2009", "TR_2008", "Alpha3", "Stdev3", "Beta3", "ExRet3", "Sharpe3", "InfoRat3", "R23", "QKYTD", "QK1Y", "QK2Y", "QK3Y", "QK4Y", "QK5Y", "QK10Y", "QK15Y", "QK2017", "QK2016", "QK2015", "QK2014", "QK2013", "QK2012", "QK2011", "QK2010", "QK2009", "QK2008", "QKAlph3", "QKStdv3", "QKBeta3", "QKExRt3", "QKShrp3", "QKInfR3", "QKRsq3p"]
	sharesAndFunds = []

	selectedAdvisorIds = []
	selectedAdvisorNames = []
	selectedMSSubAdvIds = []
	selectedMSSubAdvNames = []
	selectedMSCatIds = []
	selectedMSCatNames = []

	if request.method == "POST":
		selectedAdvisorIds = request.POST.getlist('advId')
		selectedAdvisorNames = request.POST.getlist('advName', '')
		selectedAdvisorIdSet = set(selectedAdvisorIds)

		selectedMSSubAdvIds = request.POST.getlist('subId')
		selectedMSSubAdvNames = request.POST.getlist('subName', '')
		selectedMSSubAdvIdSet = set(list(map(lambda x: int(x.encode("utf-8")), selectedMSSubAdvIds)))

		selectedMSCatIds = request.POST.getlist('catId')
		selectedMSCatNames = request.POST.getlist('catName', '')
		selectedMSCatIdSet = set(list(map(lambda x: int(x.encode("utf-8")), selectedMSCatIds)))

		start_time = time.time()
		cmpObjByAll = []

		if selectedAdvisorIds: # len() != 0, in pythonic
			for advId in selectedAdvisorIds:
				obj = Company.objects.filter(AdvisorID_id=advId).order_by("Name")
				if len(obj) == 1:
					cmpObjByAll.append(obj[0])
				elif len(obj) > 1:
					for c in obj:
						cmpObjByAll.append(c)
			print("--- 1.1 query Adv id: %s seconds ---" % (time.time() - start_time))
			print("--- 1.1 cmpObjByAll.count = %s" % len(cmpObjByAll))
			start_time = time.time()

		isResultShouldBeEmpty = False

		if selectedMSSubAdvIds:
			if cmpObjByAll:
				containMSSub = []
				qualifyId = set()
				for cmpObj in cmpObjByAll:
					subId = cmpObj.MSSubAdvId_id
					if subId in selectedMSSubAdvIdSet:
						containMSSub.append(cmpObj)
						qualifyId.add(subId)
				print("-------- 2.0 len(qualifyId) = %s, len(SubIdSet) = %s" % (len(qualifyId), len(selectedMSSubAdvIdSet)))
				if len(qualifyId) >= len(selectedMSSubAdvIdSet):
					cmpObjByAll = containMSSub
				else:
					print("------- !!! too much MSSubAdv selected, AND result should be nil...")
					cmpObjByAll = []
				isResultShouldBeEmpty = len(cmpObjByAll) == 0
				print("--- 2.1 query Sub id: %s seconds ---" % (time.time() - start_time))
				print("--- 2.1 cmpObjByAll.count = %s, isResultShouldBeEmpty = %s" % (len(cmpObjByAll), isResultShouldBeEmpty))
				start_time = time.time()
			else:
				for subId in selectedMSSubAdvIds:
					obj = Company.objects.filter(MSSubAdvId_id=subId).order_by("Name")
					if len(obj) == 1:
						cmpObjByAll.append(obj[0])
					elif len(obj) > 1:
						cmpObjByAll.extend(obj)
				print("--- 2.2 query Sub id: %s seconds ---" % (time.time() - start_time))
				print("--- 2.2 cmpObjByAll.count = %s" % len(cmpObjByAll))
				start_time = time.time()

		if selectedMSCatIds and not isResultShouldBeEmpty:
			if cmpObjByAll:
				containMSCat = []
				qualifyId = set()
				for cmpObj in cmpObjByAll:
					catId = cmpObj.MSCatDbId_id
					if catId in selectedMSCatIdSet:
						containMSCat.append(cmpObj)
						qualifyId.add(catId)
				print("-------- 3.0 len(qualifyId) = %s, len(CatIdSet) = %s" % (len(qualifyId), len(selectedMSCatIdSet)))
				if len(qualifyId) >= len(selectedMSCatIdSet):
					cmpObjByAll = containMSCat
				else:
					print("------- !!! too much MSSubAdv selected, AND result should be nil...")
					cmpObjByAll = []
				print("--- 3.1 filter Cat id: %s seconds ---" % (time.time() - start_time))
				print("--- 3.1 cmpObjByAll.count = %s" % len(cmpObjByAll))
				start_time = time.time()
			else:
				for catId in selectedMSCatIds:
					obj = Company.objects.filter(MSCatDbId_id=catId).order_by("Name")
					if len(obj) == 1:
						cmpObjByAll.append(obj[0])
					elif len(obj) > 1:
						cmpObjByAll.extend(obj)
				print("--- 3.2 query Cat id: %s seconds ---" % (time.time() - start_time))
				print("--- 3.2 cmpObjByAll.count = %s" % len(cmpObjByAll))
				start_time = time.time()

		if selectedAdvisorIds and not isResultShouldBeEmpty: # filter out the first selection result;
			qualifyId = set()
			for cmpObj in cmpObjByAll:
				qualifyId.add(cmpObj.AdvisorID_id)
			if len(qualifyId) < len(selectedAdvisorIdSet):
				print("------- 4.0 !!! too much AdvisorID_id selected, AND result should be nil...")
				cmpObjByAll = []

		companyInfo = cmpObjByAll

		# for tag Performance
		sharesAndFunds = getPerformanceInfo(companyInfo)

		selectedAdvisorNameset = set(selectedAdvisorNames)
		selectedMSSubAdvNameSet = set(selectedMSSubAdvNames)
		selectedMSCatNameSet = set(selectedMSCatNames)

		selectedAdvisorNames = []
		for advName in selectedAdvisorNameset:
			selectedAdvisorNames.append(advName.encode("utf-8"))

		selectedMSSubAdvNames = []
		for advName in selectedMSSubAdvNameSet:
			selectedMSSubAdvNames.append(advName.encode("utf-8"))

		selectedMSCatNames = []
		for catName in selectedMSCatNameSet:
			selectedMSCatNames.append(catName.encode("utf-8"))

	else:
		print "--- [GET] request is GET, init page....,"

	# for Auto-complete search lists
	advs = Advisors.objects.all()
	subs = MSSubAdvs.objects.all()
	cats = MSCats.objects.all()
	advsNames 	= list(map(lambda x: x.Name.encode("utf-8"), advs))
	subNames 	= list(map(lambda x: x.Name.encode("utf-8"), subs))
	mscatNames  = list(map(lambda x: x.Name.encode("utf-8"), cats))

	idOfAdvisorNameDict = {} # {'Name':'advId'}
	idOfMSSubAdvNameDict = {}
	idOfMSCatNameDict = {}

	for adv in advs:
		idOfAdvisorNameDict[adv.Name.encode("utf-8")] = adv.id
	for sub in subs:
		idOfMSSubAdvNameDict[sub.Name.encode("utf-8")] = sub.id
	for cat in cats:
		idOfMSCatNameDict[cat.Name.encode("utf-8")] = cat.id


	content = {
		'companys': companyInfo, # get first n rows 
		'colnames': cols,

		'advisorNames': advsNames,
		'idOfAdvisorNameDict':  idOfAdvisorNameDict,
		'selectedAdvisorIds':   selectedAdvisorIds,
		'selectedAdvisorNames': selectedAdvisorNames,

		'mssubadvNames': subNames,
		'idOfMSSubAdvNameDict':  idOfMSSubAdvNameDict,
		'selectedMSSubAdvIds':   selectedMSSubAdvIds,
		'selectedMSSubAdvNames': selectedMSSubAdvNames,

		'mscatNames': mscatNames,
		'idOfMSCatNameDict' : idOfMSCatNameDict,
		'selectedMSCatIds':   selectedMSCatIds,
		'selectedMSCatNames': selectedMSCatNames,

		'sharesAndFunds': sharesAndFunds, # for tag Performance
		'sharesAndFundsColnames': sharesAndFundsCols,
	}

	return render(request, 'blog/advisor_table.html', content)


def getPerformanceInfo(companyInfos):
	shareAndFund = []
	if len(companyInfos) == 0:
		return shareAndFund

	# The "Share" primary key is "SecID"
	# The "Fund" primary key is "FundID"
	# The two tables can link by "FundID"
	secIds = map(lambda cmpObj: cmpObj.SecId.encode("utf-8"), companyInfos)
	getShares = list(Shares.objects.filter(SecId__in=secIds))

	fundIds = map(lambda s: s.FundId.encode("utf-8"), getShares)
	getFunds = list(Funds.objects.filter(FundId__in=fundIds))

	for c in companyInfos:
		matchShare = filter(lambda s: s.SecId == c.SecId, getShares)
		matchFund  = filter(lambda f: f.FundId == c.FundId, getFunds)

		if len(matchShare) > 0 and len(matchFund) > 0:
			share = matchShare[0]
			fund = matchFund[0]
			tableRow = []
			tableRow.append(fund.Advisor)
			tableRow.append(share.FundId)
			tableRow.append(fund.MSCat)
			tableRow.append(percentage(share.TR_YTD))
			tableRow.append(percentage(share.TR_1Y))
			tableRow.append(percentage(share.TR_2Y))
			tableRow.append(percentage(share.TR_3Y))
			tableRow.append(percentage(share.TR_4Y))
			tableRow.append(percentage(share.TR_5Y))
			tableRow.append(percentage(share.TR_10Y))
			tableRow.append(percentage(share.TR_15Y))
			#tableRow.append(percentage(share.TR_2018))
			tableRow.append(percentage(share.TR_2017))
			tableRow.append(percentage(share.TR_2016))
			tableRow.append(percentage(share.TR_2015))
			tableRow.append(percentage(share.TR_2014))
			tableRow.append(percentage(share.TR_2013))
			tableRow.append(percentage(share.TR_2012))
			tableRow.append(percentage(share.TR_2011))
			tableRow.append(percentage(share.TR_2010))
			tableRow.append(percentage(share.TR_2009))
			tableRow.append(percentage(share.TR_2008))
			tableRow.append(percentage(share.Alpha3))
			tableRow.append(percentage(share.Stdev3))
			tableRow.append(percentage(share.Beta3))
			tableRow.append(percentage(share.ExRet3))
			tableRow.append(percentage(share.Sharpe3))
			tableRow.append(percentage(share.InfoRat3))
			tableRow.append(percentage(share.R23))
			tableRow.append(fund.QKYTD)
			tableRow.append(fund.QK1Y)
			tableRow.append(fund.QK2Y)
			tableRow.append(fund.QK3Y)
			tableRow.append(fund.QK4Y)
			tableRow.append(fund.QK5Y)
			tableRow.append(fund.QK10Y)
			tableRow.append(fund.QK15Y)
			#tableRow.append(fund.QK2018)
			tableRow.append(fund.QK2017)
			tableRow.append(fund.QK2016)
			tableRow.append(fund.QK2015)
			tableRow.append(fund.QK2014)
			tableRow.append(fund.QK2013)
			tableRow.append(fund.QK2012)
			tableRow.append(fund.QK2011)
			tableRow.append(fund.QK2010)
			tableRow.append(fund.QK2009)
			tableRow.append(fund.QK2008)
			tableRow.append(fund.QKAlph3)
			tableRow.append(fund.QKStdv3)
			tableRow.append(fund.QKBeta3)
			tableRow.append(fund.QKExRt3)
			tableRow.append(fund.QKShrp3)
			tableRow.append(fund.QKInfR3)
			tableRow.append(fund.QKRsq3)

			shareAndFund.append(tableRow) # list of [shareObj, fundObj]
	return shareAndFund


def percentage(val):
	rlt = "n/a"
	if val is not None:
		return "%s %%" % ('%.2f'%(val * 100))
	return rlt



def about(request):
	return render(request, 'blog/about.html')






