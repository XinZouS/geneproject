# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Funds, Shares, SubAdv
# --- use Static table ---
# from .models import Company, Advisors, MSCats, MSSubAdvs, MgrNames
# --- use FitDefault table ---
from .models import FitDefault, FitAdvisors, FitCategorys, FitSubAdvisors, FitManagerNames

import time


@login_required
def home(request):
	content = {
		# 'companys': Company.objects.all()
		# 'companys': FitDefault.objects.order_by("Name")[:10] # get first 10 rows 
	}
	return render(request, 'blog/home.html', content)



@login_required
def fit_default(request):
	openedTabId = "tabId01".encode("utf-8")

	defaultCols = ["No.","Name","Category","MF/VA","SubAdvised","Index Fund","Watch List","VIT","Fund of Funds","Inception Date","Advisor","Subadvisor","AUM","NFYTD","NF2017","NF2016","SubStart","SubSched","SubAdvEffRate","Sub_Rate($)","TR_YTD","TR_1Y","TR_2Y","TR_3Y","TR_5Y","TR_10Y","Alpha","ExcessRet","Sharpe","InfoRat","Beta","Stdev","R2","UpsideCap","DownsideCap","TrackingErr","QRK_YTD","QRK_1Y","QRK_2Y","QRK_3Y","QRK_5Y","QRK_10Y","QRK_15Y","QRK_Alpha","QRK_ExcessRet","QRK_Sharpe","QRK_InfoRat","QRK_Beta","QRK_Stdev","QRK_R2","QRK_UpsideCap","QRK_DownsideCap","QRK_TrackingErr","Team Managed","Prospectus Net Expense Ratio","Manager Name","Manager Tenure (Longest)","Manager Tenure (Average)","Benchmark"]
	companyInfo = []
	subAdvCols = ["No.", "FundId", "Fund", "SubAdvisor", "SubAdvisorParent", "AdvisorParent", "SubAdvised", "AgrmStart", "AgrmEnd", "SubStart", "SubEnd", "SubAlloc", "SubAUM", "FundAUM", "EffSub", "SubSched3"]
	subAdvs = []
	sharesAndFundsCols = ["No.", "Advisor", "FundId", "MSCat", "TR_YTD", "TR_1Y", "TR_2Y", "TR_3Y", "TR_4Y", "TR_5Y", "TR_10Y", "TR_15Y", "TR_2017", "TR_2016", "TR_2015", "TR_2014", "TR_2013", "TR_2012", "TR_2011", "TR_2010", "TR_2009", "TR_2008", "Alpha3", "Stdev3", "Beta3", "ExRet3", "Sharpe3", "InfoRat3", "R23", "QKYTD", "QK1Y", "QK2Y", "QK3Y", "QK4Y", "QK5Y", "QK10Y", "QK15Y", "QK2017", "QK2016", "QK2015", "QK2014", "QK2013", "QK2012", "QK2011", "QK2010", "QK2009", "QK2008", "QKAlph3", "QKStdv3", "QKBeta3", "QKExRt3", "QKShrp3", "QKInfR3", "QKRsq3p"]
	sharesAndFunds = []

	selectedAdvisorIds = []
	selectedAdvisorNames = []
	selectedMSSubAdvIds = []
	selectedMSSubAdvNames = []
	selectedMSCatIds = []
	selectedMSCatNames = []
	selectedMgrIds = []
	selectedMgrNames = []

	if request.method == "POST":
		selectedAdvisorIds = intListFrom(request.POST.getlist('advId'))
		selectedAdvisorNames = request.POST.getlist('advName', '')

		selectedMSSubAdvIds = intListFrom(request.POST.getlist('subId'))
		selectedMSSubAdvNames = request.POST.getlist('subName', '')

		selectedMSCatIds = intListFrom(request.POST.getlist('catId'))
		selectedMSCatNames = request.POST.getlist('catName', '')

		selectedMgrIds = intListFrom(request.POST.getlist('mgrId'))
		selectedMgrNames = request.POST.getlist('mgrName', '')

		cmpObjByAll = []

		if len(selectedAdvisorIds) + len(selectedMSSubAdvIds) + len(selectedMSCatIds) + len(selectedMgrIds) > 0:
			start_time = time.time()
			filters = Q()
			if selectedAdvisorIds:
				filters &= Q(AdvisorId_id__in=selectedAdvisorIds,)
			if selectedMSCatIds:
				filters &= Q(CategoryId_id__in=selectedMSCatIds,)
			if selectedMSSubAdvIds:
				filters &= Q(SubAdvisorId_id__in=selectedMSSubAdvIds,)
			if selectedMgrIds:
				filters &= Q(ManagerNameId_id__in=selectedMgrIds)

			cmpObjByAll = FitDefault.objects.filter(filters)
			print("--- database query finish in [ %s ] seconds ---" % (time.time() - start_time))
			print("--- get objects [ %s ] rows ---" % len(cmpObjByAll))
		else:
			print("--- Filter is empty, gets [ 0 ] rows ---")

		# === for tag Default ===
		companyInfo = formatedFitDefaultList(cmpObjByAll)

		# === for tag SubAdvisor ===
		subAdvs = getSubAdvisors(cmpObjByAll)

		# === for tag Performance ===
		sharesAndFunds = getPerformanceInfo(cmpObjByAll)

		# remove duplicates
		selectedAdvisorNameset = set(selectedAdvisorNames)
		selectedMSSubAdvNameSet = set(selectedMSSubAdvNames)
		selectedMSCatNameSet = set(selectedMSCatNames)
		selectedMgrNameSet = set(selectedMgrNames)

		selectedAdvisorNames 	= list(map(lambda x: x.encode("utf-8"), selectedAdvisorNameset))
		selectedMSSubAdvNames 	= list(map(lambda x: x.encode("utf-8"), selectedMSSubAdvNameSet))
		selectedMSCatNames 		= list(map(lambda x: x.encode("utf-8"), selectedMSCatNameSet))
		selectedMgrNames 		= list(map(lambda x: x.encode("utf-8"), selectedMgrNameSet))

		# TODO: try get 'opendTabInput' without getlist:
		lastTabId = request.POST.getlist('openedTabInput')
		if lastTabId and len(lastTabId) > 0:
			openedTabId = lastTabId[0].encode("utf-8")

		isSave = request.POST.get('isSaveCheckbox')
		if isSave:
			print("save!!!!!!!")
		else:
			print("noooooo")
	else:
		print "--- [GET] request is GET, init page....,"

	# for Auto-complete search lists
	advs = FitAdvisors.objects.all()
	subs = FitSubAdvisors.objects.all()
	cats = FitCategorys.objects.all()
	mgrs = FitManagerNames.objects.all()
	advsNames 	= list(map(lambda x: x.Name.encode("utf-8"), advs))
	subNames 	= list(map(lambda x: x.Name.encode("utf-8"), subs))
	mscatNames  = list(map(lambda x: x.Name.encode("utf-8"), cats))
	mgrNames    = list(map(lambda x: x.Name.encode("utf-8"), mgrs))
	idOfAdvisorNameDict = {} # {'Name':'advId'}
	idOfMSSubAdvNameDict = {}
	idOfMSCatNameDict = {}
	idOfMgrNameDict = {}
	for adv in advs:
		idOfAdvisorNameDict[adv.Name.encode("utf-8")] = adv.id
	for sub in subs:
		idOfMSSubAdvNameDict[sub.Name.encode("utf-8")] = sub.id
	for cat in cats:
		idOfMSCatNameDict[cat.Name.encode("utf-8")] = cat.id
	for mgr in mgrs:
		idOfMgrNameDict[mgr.Name.encode("utf-8")] = mgr.id


	content = {
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

		'mgrNames': mgrNames,
		'idOfMgrNameDict' : idOfMgrNameDict,
		'selectedMgrIds':   selectedMgrIds,
		'selectedMgrNames': selectedMgrNames,

		'openedTabId': [openedTabId],

		'colnames': defaultCols,
		'companys': companyInfo,

		'subAdvCols': subAdvCols,
		'subAdvs': subAdvs,

		'sharesAndFunds': sharesAndFunds, # for tag Performance
		'sharesAndFundsColnames': sharesAndFundsCols,
	}

	return render(request, 'blog/advisor_table.html', content)


def intListFrom(aList):
	rltList = []
	for string in aList:
		try:
			num = int(string.encode("utf-8"))
			rltList.append(num)
		except ValueError as e:
			print("-------- [ERROR] type error SKIPPING string: [%s --> int failed] " % string)
			print(e)
			continue
	return rltList


def formatedFitDefaultList(companyInfos):
	fitList = []

	for c in companyInfos:
		row = []
		row.append(c.Name)
		row.append(c.Category)
		row.append(c.MFVA)
		row.append(c.SubAdvised)
		row.append(c.IndexFund)
		row.append(c.WatchList)
		row.append(c.VIT)
		row.append(c.FundOfFunds)
		row.append(c.InceptionDate)
		row.append(c.Advisor)
		row.append(c.SubAdvisor)
		row.append(toInt(c.AUM))
		row.append(toInt(c.NFYTD))
		row.append(toInt(c.NF2017))
		row.append(toInt(c.NF2016))
		row.append(c.SubStart)
		row.append(c.SubSched)
		row.append(percentage(c.SubAdvEffRate))
		row.append(percentage(c.SubRate))
		row.append([percentage(c.TR_YTD), c.QRK_YTD]) # counter = 20
		row.append([percentage(c.TR_1Y), c.QRK_1Y])
		row.append([percentage(c.TR_2Y), c.QRK_2Y])
		row.append([percentage(c.TR_3Y), c.QRK_3Y])
		row.append([percentage(c.TR_5Y), c.QRK_5Y])
		row.append([percentage(c.TR_10Y), c.QRK_10Y])
		row.append([percentage(c.Alpha), c.QRK_Alpha])
		row.append([percentage(c.ExcessRet), c.QRK_ExcessRet])
		row.append([percentage(c.Sharpe), c.QRK_Sharpe])
		row.append([percentage(c.InfoRat), c.QRK_InfoRat])
		row.append([percentage(c.Beta), c.QRK_Beta]) # cnt = 30
		row.append([percentage(c.Stdev), c.QRK_Stdev])
		row.append([percentage(c.R2), c.QRK_R2])
		row.append([toInt(c.UpsideCap), c.QRK_UpsideCap])
		row.append([toInt(c.DownsideCap), c.QRK_DownsideCap])
		row.append([percentage(c.TrackingErr), c.QRK_TrackingErr]) # counter = 35
		row.append(c.QRK_YTD)
		row.append(c.QRK_1Y)
		row.append(c.QRK_2Y)
		row.append(c.QRK_3Y)
		row.append(c.QRK_5Y)
		row.append(c.QRK_10Y)
		row.append(c.QRK_15Y)
		row.append(c.QRK_Alpha)
		row.append(c.QRK_ExcessRet)
		row.append(c.QRK_Sharpe)
		row.append(c.QRK_InfoRat)
		row.append(c.QRK_Beta)
		row.append(c.QRK_Stdev)
		row.append(c.QRK_R2)
		row.append(c.QRK_UpsideCap)
		row.append(c.QRK_DownsideCap)
		row.append(c.QRK_TrackingErr)
		row.append(c.TeamManaged)
		row.append(toFloat_2(c.ProspectusNetExpenseRatio))
		row.append(c.ManagerName)
		row.append(toFloat_2(c.ManagerTenureLongest))
		row.append(toFloat_2(c.ManagerTenureAverage))
		row.append(c.Benchmark) # 58, the last col to display
		# row.append(c.SecId)
		# row.append(c.FundId)

		fitList.append(row)

	return fitList


def getSubAdvisors(companyInfos):
	subAdvs = []
	if len(companyInfos) == 0:
		return subAdvs

	fundIds = list(map(lambda cmpObj: cmpObj.FundId.encode("utf-8"), companyInfos))
	getSubAdvs = SubAdv.objects.filter(FundId__in=fundIds)

	for s in getSubAdvs:
		row = []
		row.append(s.FundId)
		row.append(s.Fund)
		row.append(s.SubAdvisor)
		row.append(s.SubAdvisorParent)
		row.append(s.AdvisorParent)
		row.append(s.SubAdvised)
		row.append(s.AgrmStart)
		row.append(s.AgrmEnd)
		row.append(s.SubStart)
		row.append(s.SubEnd)
		row.append(s.SubAlloc)
		row.append(s.SubAUM)
		row.append(s.FundAUM)
		row.append(s.EffSub)
		row.append(s.SubSched3)

		subAdvs.append(row)

	return subAdvs


def getPerformanceInfo(companyInfos):
	shareAndFund = []
	if len(companyInfos) == 0:
		return shareAndFund

	# The "Share" primary key is "SecId"
	# The "Fund" primary key is "FundId"
	# The two tables can link by "FundId"
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
			row = []
			row.append(fund.Advisor)
			row.append(share.FundId)
			row.append(fund.MSCat)
			row.append([percentage(share.TR_YTD), fund.QKYTD]) # forloop.counter = 4
			row.append([percentage(share.TR_1Y), fund.QK1Y])
			row.append([percentage(share.TR_2Y), fund.QK2Y])
			row.append([percentage(share.TR_3Y), fund.QK3Y])
			row.append([percentage(share.TR_4Y), fund.QK4Y])
			row.append([percentage(share.TR_5Y), fund.QK5Y])
			row.append([percentage(share.TR_10Y), fund.QK10Y]) # forloop.counter = 10
			row.append([percentage(share.TR_15Y), fund.QK15Y])
			#row.append([percentage(share.TR_2018), fund.QK2018Y])
			row.append([percentage(share.TR_2017), fund.QK2017])
			row.append([percentage(share.TR_2016), fund.QK2016])
			row.append([percentage(share.TR_2015), fund.QK2015])
			row.append([percentage(share.TR_2014), fund.QK2014])
			row.append([percentage(share.TR_2013), fund.QK2013])
			row.append([percentage(share.TR_2012), fund.QK2012])
			row.append([percentage(share.TR_2011), fund.QK2011])
			row.append([percentage(share.TR_2010), fund.QK2010])
			row.append([percentage(share.TR_2009), fund.QK2009]) # forloop.counter = 20
			row.append([percentage(share.TR_2008), fund.QK2008])
			row.append([percentage(share.Alpha3), fund.QKAlph3])
			row.append([percentage(share.Stdev3), fund.QKStdv3])
			row.append([percentage(share.Beta3), fund.QKBeta3])
			row.append([percentage(share.ExRet3), fund.QKExRt3])
			row.append([percentage(share.Sharpe3), fund.QKShrp3])
			row.append([percentage(share.InfoRat3), fund.QKInfR3])
			row.append([percentage(share.R23), fund.QKRsq3]) # forloop.counter = 29
			row.append(fund.QKYTD)
			row.append(fund.QK1Y)
			row.append(fund.QK2Y)
			row.append(fund.QK3Y)
			row.append(fund.QK4Y)
			row.append(fund.QK5Y)
			row.append(fund.QK10Y)
			row.append(fund.QK15Y)
			#row.append(fund.QK2018)
			row.append(fund.QK2017)
			row.append(fund.QK2016)
			row.append(fund.QK2015)
			row.append(fund.QK2014)
			row.append(fund.QK2013)
			row.append(fund.QK2012)
			row.append(fund.QK2011)
			row.append(fund.QK2010)
			row.append(fund.QK2009)
			row.append(fund.QK2008)
			row.append(fund.QKAlph3)
			row.append(fund.QKStdv3)
			row.append(fund.QKBeta3)
			row.append(fund.QKExRt3)
			row.append(fund.QKShrp3)
			row.append(fund.QKInfR3)
			row.append(fund.QKRsq3)

			shareAndFund.append(row) # list of [shareObj, fundObj]
	return shareAndFund


def percentage(val):
	if val is not None:
		return "%s %%" % ('%.2f'%(val * 100))
	return "n/a"

def toFloat_2(val):
	if val is not None:
		return '%.2f' % val

def toInt(val):
	if val is not None:
		return int(val)
	return "n/a"


def about(request):
	return render(request, 'blog/about.html')






