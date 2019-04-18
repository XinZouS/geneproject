# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Funds, Shares
# --- use Static table ---
# from .models import Company, Advisors, MSCats, MSSubAdvs, MgrNames
# --- use FitDefault table ---
from .models import FitDefault, FitAdvisors, FitCategorys, FitSubAdvisors, FitManagerNames

import time


@login_required
def home(request):
	content = {
		# 'companys': Company.objects.all()
		'companys': FitDefault.objects.order_by("Name")[:10] # get first 10 rows 
	}
	return render(request, 'blog/home.html', content)


# @login_required
# def advisor_table(request):
# 	cols = ["No.", "Name", "CUSIP", "SecId", "FundId", "Advisor", "MSCat", "MSSubAdv"]
# 	companyInfo = []
# 	sharesAndFundsCols = ["No.", "Advisor", "FundId", "MSCat", "TR_YTD", "TR_1Y", "TR_2Y", "TR_3Y", "TR_4Y", "TR_5Y", "TR_10Y", "TR_15Y", "TR_2017", "TR_2016", "TR_2015", "TR_2014", "TR_2013", "TR_2012", "TR_2011", "TR_2010", "TR_2009", "TR_2008", "Alpha3", "Stdev3", "Beta3", "ExRet3", "Sharpe3", "InfoRat3", "R23", "QKYTD", "QK1Y", "QK2Y", "QK3Y", "QK4Y", "QK5Y", "QK10Y", "QK15Y", "QK2017", "QK2016", "QK2015", "QK2014", "QK2013", "QK2012", "QK2011", "QK2010", "QK2009", "QK2008", "QKAlph3", "QKStdv3", "QKBeta3", "QKExRt3", "QKShrp3", "QKInfR3", "QKRsq3p"]
# 	sharesAndFunds = []

# 	selectedAdvisorIds = []
# 	selectedAdvisorNames = []
# 	selectedMSSubAdvIds = []
# 	selectedMSSubAdvNames = []
# 	selectedMSCatIds = []
# 	selectedMSCatNames = []
# 	selectedMgrIds = []
# 	selectedMgrNames = []

# 	if request.method == "POST":
# 		selectedAdvisorIds = intListFrom(request.POST.getlist('advId'))
# 		selectedAdvisorNames = request.POST.getlist('advName', '')
# 		selectedAdvisorIdSet = set(selectedAdvisorIds)

# 		selectedMSSubAdvIds = intListFrom(request.POST.getlist('subId'))
# 		selectedMSSubAdvNames = request.POST.getlist('subName', '')
# 		selectedMSSubAdvIdSet = set(selectedMSSubAdvIds) #set(list(map(lambda x: int(x), selectedMSSubAdvIds)))

# 		selectedMSCatIds = intListFrom(request.POST.getlist('catId'))
# 		selectedMSCatNames = request.POST.getlist('catName', '')
# 		selectedMSCatIdSet = set(selectedMSCatIds) #set(list(map(lambda x: int(x.encode("utf-8")), selectedMSCatIds)))

# 		selectedMgrIds = intListFrom(request.POST.getlist('mgrId'))
# 		selectedMgrNames = request.POST.getlist('mgrName', '')
# 		selectedMgrIdSet = set(selectedMgrIds) #set(list(map(lambda x: int(x.encode("utf-8")), selectedMgrIds)))
# 		print(selectedMgrIds)

# 		start_time = time.time()
# 		cmpObjByAll = []

# 		if selectedAdvisorIds: # len() != 0, in pythonic
# 			for advId in selectedAdvisorIds:
# 				obj = Company.objects.filter(AdvisorID_id=advId).order_by("Name")
# 				if len(obj) == 1:
# 					cmpObjByAll.append(obj[0])
# 				elif len(obj) > 1:
# 					for c in obj:
# 						cmpObjByAll.append(c)
# 			print("--- 1.1 query Adv id: %s seconds ---" % (time.time() - start_time))
# 			print("--- 1.1 cmpObjByAll.count = %s" % len(cmpObjByAll))
# 			start_time = time.time()

# 		isResultShouldBeEmpty = False

# 		if selectedMSSubAdvIds:
# 			if cmpObjByAll:
# 				containMSSub = []
# 				qualifyId = set()
# 				for cmpObj in cmpObjByAll:
# 					subId = cmpObj.MSSubAdvId_id
# 					if subId in selectedMSSubAdvIdSet:
# 						containMSSub.append(cmpObj)
# 						qualifyId.add(subId)
# 				print("-------- 2.0 len(qualifyId) = %s, len(SubIdSet) = %s" % (len(qualifyId), len(selectedMSSubAdvIdSet)))
# 				# if len(qualifyId) >= len(selectedMSSubAdvIdSet):
# 				cmpObjByAll = containMSSub
# 				# else:
# 				# 	print("------- !!! too much MSSubAdv selected, AND result should be nil...")
# 				# 	cmpObjByAll = []
# 				# isResultShouldBeEmpty = len(cmpObjByAll) == 0
# 				print("--- 2.1 query Sub id: %s seconds ---" % (time.time() - start_time))
# 				print("--- 2.1 cmpObjByAll.count = %s, isResultShouldBeEmpty = %s" % (len(cmpObjByAll), isResultShouldBeEmpty))
# 				start_time = time.time()
# 			else:
# 				for subId in selectedMSSubAdvIds:
# 					obj = Company.objects.filter(MSSubAdvId_id=subId).order_by("Name")
# 					if len(obj) == 1:
# 						cmpObjByAll.append(obj[0])
# 					elif len(obj) > 1:
# 						cmpObjByAll.extend(obj)
# 				print("--- 2.2 query Sub id: %s seconds ---" % (time.time() - start_time))
# 				print("--- 2.2 cmpObjByAll.count = %s" % len(cmpObjByAll))
# 				start_time = time.time()

# 		if selectedMSCatIds and not isResultShouldBeEmpty:
# 			if cmpObjByAll:
# 				containMSCat = []
# 				qualifyId = set()
# 				for cmpObj in cmpObjByAll:
# 					catId = cmpObj.MSCatDbId_id
# 					if catId in selectedMSCatIdSet:
# 						containMSCat.append(cmpObj)
# 						qualifyId.add(catId)
# 				print("-------- 3.0 len(qualifyId) = %s, len(CatIdSet) = %s" % (len(qualifyId), len(selectedMSCatIdSet)))
# 				# if len(qualifyId) >= len(selectedMSCatIdSet):
# 				cmpObjByAll = containMSCat
# 				# else:
# 				# 	print("------- !!! too much MSSubAdv selected, AND result should be nil...")
# 				# 	cmpObjByAll = []
# 				# isResultShouldBeEmpty = len(cmpObjByAll) == 0
# 				print("--- 3.1 filter Cat id: %s seconds ---" % (time.time() - start_time))
# 				print("--- 3.1 cmpObjByAll.count = %s, isResultShouldBeEmpty = %s" % (len(cmpObjByAll), isResultShouldBeEmpty))
# 				start_time = time.time()
# 			else:
# 				for catId in selectedMSCatIds:
# 					obj = Company.objects.filter(MSCatDbId_id=catId).order_by("Name")
# 					if len(obj) == 1:
# 						cmpObjByAll.append(obj[0])
# 					elif len(obj) > 1:
# 						cmpObjByAll.extend(obj)
# 				print("--- 3.2 query Cat id: %s seconds ---" % (time.time() - start_time))
# 				print("--- 3.2 cmpObjByAll.count = %s" % len(cmpObjByAll))
# 				start_time = time.time()

# 		if selectedMgrIds and not isResultShouldBeEmpty:
# 			if cmpObjByAll:
# 				containMgr = []
# 				qualifyId = set()
# 				for cmpObj in cmpObjByAll:
# 					mgrId = cmpObj.MgrNameId_id
# 					if mgrId in selectedMgrIdSet:
# 						containMgr.append(cmpObj)
# 						qualifyId.add(mgrId)
# 				print("-------- 4.0 len(qualifyId) = %s, len(MgrIdSet) = %s" % (len(qualifyId), len(selectedMgrIdSet)))
# 				# if len(qualifyId) >= len(selectedMgrIdSet):
# 				cmpObjByAll = containMgr
# 				# else:
# 				# 	print("------- !!! too much MgrNames selected, AND result should be nil...")
# 				# 	cmpObjByAll = []
# 				# isResultShouldBeEmpty = len(cmpObjByAll) == 0
# 				print("--- 4.1 filter Cat id: %s seconds ---" % (time.time() - start_time))
# 				print("--- 4.1 cmpObjByAll.count = %s" % len(cmpObjByAll))
# 				start_time = time.time()
# 			else:
# 				for mgrId in selectedMgrIds:
# 					obj = Company.objects.filter(MgrNameId_id=mgrId).order_by("Name")
# 					if len(obj) == 1:
# 						cmpObjByAll.append(obj[0])
# 					elif len(obj) > 1:
# 						cmpObjByAll.extend(obj)
# 				print("--- 4.2 query Mgr id: %s seconds ---" % (time.time() - start_time))
# 				print("--- 4.2 cmpObjByAll.count = %s" % len(cmpObjByAll))
# 				start_time = time.time()

# 		# if selectedAdvisorIds and not isResultShouldBeEmpty: # filter out the first selection result;
# 		# 	qualifyId = set()
# 		# 	for cmpObj in cmpObjByAll:
# 		# 		qualifyId.add(cmpObj.AdvisorID_id)
# 		# 	if len(qualifyId) < len(selectedAdvisorIdSet):
# 		# 		print("------- 4.0 !!! too much AdvisorID_id selected, AND result should be nil...")
# 		# 		cmpObjByAll = []

# 		companyInfo = cmpObjByAll

# 		# for tag Performance
# 		sharesAndFunds = getPerformanceInfo(companyInfo)

# 		selectedAdvisorNameset = set(selectedAdvisorNames)
# 		selectedMSSubAdvNameSet = set(selectedMSSubAdvNames)
# 		selectedMSCatNameSet = set(selectedMSCatNames)
# 		selectedMgrNameSet = set(selectedMgrNames)

# 		selectedAdvisorNames = []
# 		for advName in selectedAdvisorNameset:
# 			selectedAdvisorNames.append(advName.encode("utf-8"))

# 		selectedMSSubAdvNames = []
# 		for advName in selectedMSSubAdvNameSet:
# 			selectedMSSubAdvNames.append(advName.encode("utf-8"))

# 		selectedMSCatNames = []
# 		for catName in selectedMSCatNameSet:
# 			selectedMSCatNames.append(catName.encode("utf-8"))

# 		selectedMgrNames = []
# 		for mgrName in selectedMgrNameSet:
# 			selectedMgrNames.append(mgrName.encode("utf-8"))

# 	else:
# 		print "--- [GET] request is GET, init page....,"

# 	# for Auto-complete search lists
# 	advs = Advisors.objects.all()
# 	subs = MSSubAdvs.objects.all()
# 	cats = MSCats.objects.all()
# 	mgrs = MgrNames.objects.all()
# 	advsNames 	= list(map(lambda x: x.Name.encode("utf-8"), advs))
# 	subNames 	= list(map(lambda x: x.Name.encode("utf-8"), subs))
# 	mscatNames  = list(map(lambda x: x.Name.encode("utf-8"), cats))
# 	mgrNames    = list(map(lambda x: x.Name.encode("utf-8"), mgrs))

# 	idOfAdvisorNameDict = {} # {'Name':'advId'}
# 	idOfMSSubAdvNameDict = {}
# 	idOfMSCatNameDict = {}
# 	idOfMgrNameDict = {}

# 	for adv in advs:
# 		idOfAdvisorNameDict[adv.Name.encode("utf-8")] = adv.id
# 	for sub in subs:
# 		idOfMSSubAdvNameDict[sub.Name.encode("utf-8")] = sub.id
# 	for cat in cats:
# 		idOfMSCatNameDict[cat.Name.encode("utf-8")] = cat.id
# 	for mgr in mgrs:
# 		idOfMgrNameDict[mgr.Name.encode("utf-8")] = mgr.id


# 	content = {
# 		'companys': companyInfo, # get first n rows 
# 		'colnames': cols,

# 		'advisorNames': advsNames,
# 		'idOfAdvisorNameDict':  idOfAdvisorNameDict,
# 		'selectedAdvisorIds':   selectedAdvisorIds,
# 		'selectedAdvisorNames': selectedAdvisorNames,

# 		'mssubadvNames': subNames,
# 		'idOfMSSubAdvNameDict':  idOfMSSubAdvNameDict,
# 		'selectedMSSubAdvIds':   selectedMSSubAdvIds,
# 		'selectedMSSubAdvNames': selectedMSSubAdvNames,

# 		'mscatNames': mscatNames,
# 		'idOfMSCatNameDict' : idOfMSCatNameDict,
# 		'selectedMSCatIds':   selectedMSCatIds,
# 		'selectedMSCatNames': selectedMSCatNames,

# 		'mgrNames': mgrNames,
# 		'idOfMgrNameDict' : idOfMgrNameDict,
# 		'selectedMgrIds':   selectedMgrIds,
# 		'selectedMgrNames': selectedMgrNames,

# 		'sharesAndFunds': sharesAndFunds, # for tag Performance
# 		'sharesAndFundsColnames': sharesAndFundsCols,
# 	}

# 	return render(request, 'blog/advisor_table.html', content)


@login_required
def fit_default(request):
	cols = ["No.","Name","Category","MF/VA","SubAdvised","Index Fund","Watch_List","VIT","Fund of Funds","Inception Date","Advisor","Subadvisor","AUM","NFYTD","NF2017","NF2016","TR_YTD","TR_1y","TR_2y","TR_3y","TR_5y","TR_10y","SubStart","SubSched","SubAdvEffRate","Sub_Rate($)","Alpha","ExcessRet","Sharpe","InfoRat","Beta","Stdev","R2","UpsideCap","DownsideCap","TrackingErr","QRK_YTD","QRK_1y","QRK_2y","QRK_3y","QRK_5y","QRK_10y","QRK_15y","QRK_Alpha","QRK_ExcessRet","QRK_Sharpe","QRK_InfoRat","QRK_Beta","QRK_Stdev","QRK_R2","QRK_UpsideCap","QRK_DownsideCap","QRK_TrackingErr","Team Managed","Prospectus Net Expense Ratio","Manager Name","Manager Tenure (Longest)","Manager Tenure (Average)","Benchmark"]
	companyInfo = []
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
		selectedAdvisorIdSet = set(selectedAdvisorIds)

		selectedMSSubAdvIds = intListFrom(request.POST.getlist('subId'))
		selectedMSSubAdvNames = request.POST.getlist('subName', '')
		selectedMSSubAdvIdSet = set(selectedMSSubAdvIds) #set(list(map(lambda x: int(x), selectedMSSubAdvIds)))

		selectedMSCatIds = intListFrom(request.POST.getlist('catId'))
		selectedMSCatNames = request.POST.getlist('catName', '')
		selectedMSCatIdSet = set(selectedMSCatIds) #set(list(map(lambda x: int(x.encode("utf-8")), selectedMSCatIds)))

		selectedMgrIds = intListFrom(request.POST.getlist('mgrId'))
		selectedMgrNames = request.POST.getlist('mgrName', '')
		selectedMgrIdSet = set(selectedMgrIds) #set(list(map(lambda x: int(x.encode("utf-8")), selectedMgrIds)))
		print(selectedMgrIds)

		start_time = time.time()
		cmpObjByAll = []

		if selectedAdvisorIds: # len() != 0, in pythonic
			for advId in selectedAdvisorIds:
				obj = FitDefault.objects.filter(AdvisorId_id=advId).order_by("Name")
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
				# if len(qualifyId) >= len(selectedMSSubAdvIdSet):
				cmpObjByAll = containMSSub
				# else:
				# 	print("------- !!! too much MSSubAdv selected, AND result should be nil...")
				# 	cmpObjByAll = []
				# isResultShouldBeEmpty = len(cmpObjByAll) == 0
				print("--- 2.1 query Sub id: %s seconds ---" % (time.time() - start_time))
				print("--- 2.1 cmpObjByAll.count = %s, isResultShouldBeEmpty = %s" % (len(cmpObjByAll), isResultShouldBeEmpty))
				start_time = time.time()
			else:
				for subId in selectedMSSubAdvIds:
					obj = FitDefault.objects.filter(SubAdvisorId_id=subId).order_by("Name")
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
				# if len(qualifyId) >= len(selectedMSCatIdSet):
				cmpObjByAll = containMSCat
				# else:
				# 	print("------- !!! too much MSSubAdv selected, AND result should be nil...")
				# 	cmpObjByAll = []
				# isResultShouldBeEmpty = len(cmpObjByAll) == 0
				print("--- 3.1 filter Cat id: %s seconds ---" % (time.time() - start_time))
				print("--- 3.1 cmpObjByAll.count = %s, isResultShouldBeEmpty = %s" % (len(cmpObjByAll), isResultShouldBeEmpty))
				start_time = time.time()
			else:
				for catId in selectedMSCatIds:
					obj = FitDefault.objects.filter(CategoryId_id=catId).order_by("Name")
					if len(obj) == 1:
						cmpObjByAll.append(obj[0])
					elif len(obj) > 1:
						cmpObjByAll.extend(obj)
				print("--- 3.2 query Cat id: %s seconds ---" % (time.time() - start_time))
				print("--- 3.2 cmpObjByAll.count = %s" % len(cmpObjByAll))
				start_time = time.time()

		if selectedMgrIds and not isResultShouldBeEmpty:
			if cmpObjByAll:
				containMgr = []
				qualifyId = set()
				for cmpObj in cmpObjByAll:
					mgrId = cmpObj.MgrNameId_id
					if mgrId in selectedMgrIdSet:
						containMgr.append(cmpObj)
						qualifyId.add(mgrId)
				print("-------- 4.0 len(qualifyId) = %s, len(MgrIdSet) = %s" % (len(qualifyId), len(selectedMgrIdSet)))
				# if len(qualifyId) >= len(selectedMgrIdSet):
				cmpObjByAll = containMgr
				# else:
				# 	print("------- !!! too much MgrNames selected, AND result should be nil...")
				# 	cmpObjByAll = []
				# isResultShouldBeEmpty = len(cmpObjByAll) == 0
				print("--- 4.1 filter Cat id: %s seconds ---" % (time.time() - start_time))
				print("--- 4.1 cmpObjByAll.count = %s" % len(cmpObjByAll))
				start_time = time.time()
			else:
				for mgrId in selectedMgrIds:
					obj = FitDefault.objects.filter(ManagerNameId_id=mgrId).order_by("Name")
					if len(obj) == 1:
						cmpObjByAll.append(obj[0])
					elif len(obj) > 1:
						cmpObjByAll.extend(obj)
				print("--- 4.2 query Mgr id: %s seconds ---" % (time.time() - start_time))
				print("--- 4.2 cmpObjByAll.count = %s" % len(cmpObjByAll))
				start_time = time.time()

		# if selectedAdvisorIds and not isResultShouldBeEmpty: # filter out the first selection result;
		# 	qualifyId = set()
		# 	for cmpObj in cmpObjByAll:
		# 		qualifyId.add(cmpObj.AdvisorID_id)
		# 	if len(qualifyId) < len(selectedAdvisorIdSet):
		# 		print("------- 4.0 !!! too much AdvisorID_id selected, AND result should be nil...")
		# 		cmpObjByAll = []

		companyInfo = formatedFitDefaultList(cmpObjByAll)

		# for tag Performance
		# sharesAndFunds = getPerformanceInfo(companyInfo)

		selectedAdvisorNameset = set(selectedAdvisorNames)
		selectedMSSubAdvNameSet = set(selectedMSSubAdvNames)
		selectedMSCatNameSet = set(selectedMSCatNames)
		selectedMgrNameSet = set(selectedMgrNames)

		selectedAdvisorNames = []
		for advName in selectedAdvisorNameset:
			selectedAdvisorNames.append(advName.encode("utf-8"))

		selectedMSSubAdvNames = []
		for advName in selectedMSSubAdvNameSet:
			selectedMSSubAdvNames.append(advName.encode("utf-8"))

		selectedMSCatNames = []
		for catName in selectedMSCatNameSet:
			selectedMSCatNames.append(catName.encode("utf-8"))

		selectedMgrNames = []
		for mgrName in selectedMgrNameSet:
			selectedMgrNames.append(mgrName.encode("utf-8"))

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

		'mgrNames': mgrNames,
		'idOfMgrNameDict' : idOfMgrNameDict,
		'selectedMgrIds':   selectedMgrIds,
		'selectedMgrNames': selectedMgrNames,

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
		row.append(percentage(c.AUM))
		row.append(percentage(c.NFYTD))
		row.append(percentage(c.NF2017))
		row.append(percentage(c.NF2016))
		row.append(percentage(c.TR_YTD))
		row.append(percentage(c.TR_1Y))
		row.append(percentage(c.TR_2Y))
		row.append(percentage(c.TR_3Y))
		row.append(percentage(c.TR_5Y))
		row.append(percentage(c.TR_10Y))
		row.append(c.SubStart)
		row.append(c.SubSched)
		row.append(percentage(c.SubAdvEffRate))
		row.append(percentage(c.SubRate))
		row.append(percentage(c.Alpha))
		row.append(percentage(c.ExcessRet))
		row.append(percentage(c.Sharpe))
		row.append(percentage(c.InfoRat))
		row.append(percentage(c.Beta))
		row.append(percentage(c.Stdev))
		row.append(percentage(c.R2))
		row.append(percentage(c.UpsideCap))
		row.append(percentage(c.DownsideCap))
		row.append(percentage(c.TrackingErr))
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
		row.append(percentage(c.ProspectusNetExpenseRatio))
		row.append(c.ManagerName)
		row.append(c.ManagerTenureLongest)
		row.append(c.ManagerTenureAverage)
		row.append(c.Benchmark)

		fitList.append(row)

	return fitList


def getPerformanceInfo(companyInfos):
	shareAndFund = []
	# if len(companyInfos) == 0:
	# 	return shareAndFund

	# # The "Share" primary key is "SecID"
	# # The "Fund" primary key is "FundID"
	# # The two tables can link by "FundID"
	# secIds = map(lambda cmpObj: cmpObj.SecId.encode("utf-8"), companyInfos)
	# getShares = list(Shares.objects.filter(SecId__in=secIds))

	# fundIds = map(lambda s: s.FundId.encode("utf-8"), getShares)
	# getFunds = list(Funds.objects.filter(FundId__in=fundIds))

	# for c in companyInfos:
	# 	matchShare = filter(lambda s: s.SecId == c.SecId, getShares)
	# 	matchFund  = filter(lambda f: f.FundId == c.FundId, getFunds)

	# 	if len(matchShare) > 0 and len(matchFund) > 0:
	# 		share = matchShare[0]
	# 		fund = matchFund[0]
	# 		tableRow = []
	# 		tableRow.append(fund.Advisor)
	# 		tableRow.append(share.FundId)
	# 		tableRow.append(fund.MSCat)
	# 		tableRow.append([percentage(share.TR_YTD), fund.QKYTD]) # forloop.counter = 4
	# 		tableRow.append([percentage(share.TR_1Y), fund.QK1Y])
	# 		tableRow.append([percentage(share.TR_2Y), fund.QK2Y])
	# 		tableRow.append([percentage(share.TR_3Y), fund.QK3Y])
	# 		tableRow.append([percentage(share.TR_4Y), fund.QK4Y])
	# 		tableRow.append([percentage(share.TR_5Y), fund.QK5Y])
	# 		tableRow.append([percentage(share.TR_10Y), fund.QK10Y])
	# 		tableRow.append([percentage(share.TR_15Y), fund.QK15Y])
	# 		#tableRow.append([percentage(share.TR_2018), fund.QK2018Y])
	# 		tableRow.append([percentage(share.TR_2017), fund.QK2017])
	# 		tableRow.append([percentage(share.TR_2016), fund.QK2016])
	# 		tableRow.append([percentage(share.TR_2015), fund.QK2015])
	# 		tableRow.append([percentage(share.TR_2014), fund.QK2014])
	# 		tableRow.append([percentage(share.TR_2013), fund.QK2013])
	# 		tableRow.append([percentage(share.TR_2012), fund.QK2012])
	# 		tableRow.append([percentage(share.TR_2011), fund.QK2011])
	# 		tableRow.append([percentage(share.TR_2010), fund.QK2010])
	# 		tableRow.append([percentage(share.TR_2009), fund.QK2009])
	# 		tableRow.append([percentage(share.TR_2008), fund.QK2008])
	# 		tableRow.append([percentage(share.Alpha3), fund.QKAlph3])
	# 		tableRow.append([percentage(share.Stdev3), fund.QKStdv3])
	# 		tableRow.append([percentage(share.Beta3), fund.QKBeta3])
	# 		tableRow.append([percentage(share.ExRet3), fund.QKExRt3])
	# 		tableRow.append([percentage(share.Sharpe3), fund.QKShrp3])
	# 		tableRow.append([percentage(share.InfoRat3), fund.QKInfR3])
	# 		tableRow.append([percentage(share.R23), fund.QKRsq3]) # forloop.counter = 29
	# 		tableRow.append(fund.QKYTD)
	# 		tableRow.append(fund.QK1Y)
	# 		tableRow.append(fund.QK2Y)
	# 		tableRow.append(fund.QK3Y)
	# 		tableRow.append(fund.QK4Y)
	# 		tableRow.append(fund.QK5Y)
	# 		tableRow.append(fund.QK10Y)
	# 		tableRow.append(fund.QK15Y)
	# 		#tableRow.append(fund.QK2018)
	# 		tableRow.append(fund.QK2017)
	# 		tableRow.append(fund.QK2016)
	# 		tableRow.append(fund.QK2015)
	# 		tableRow.append(fund.QK2014)
	# 		tableRow.append(fund.QK2013)
	# 		tableRow.append(fund.QK2012)
	# 		tableRow.append(fund.QK2011)
	# 		tableRow.append(fund.QK2010)
	# 		tableRow.append(fund.QK2009)
	# 		tableRow.append(fund.QK2008)
	# 		tableRow.append(fund.QKAlph3)
	# 		tableRow.append(fund.QKStdv3)
	# 		tableRow.append(fund.QKBeta3)
	# 		tableRow.append(fund.QKExRt3)
	# 		tableRow.append(fund.QKShrp3)
	# 		tableRow.append(fund.QKInfR3)
	# 		tableRow.append(fund.QKRsq3)

	# 		shareAndFund.append(tableRow) # list of [shareObj, fundObj]
	return shareAndFund


def percentage(val):
	rlt = "n/a"
	if val is not None:
		return "%s %%" % ('%.2f'%(val * 100))
	return rlt



def about(request):
	return render(request, 'blog/about.html')






