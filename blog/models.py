# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Advisors(models.Model):  # model name must NOT the same as column name!
	Name = models.CharField(max_length=400,null=False)

	def __str__(self):
		return self.Name


class MSCats(models.Model):  # model name must NOT the same as column name!
	Name = models.CharField(max_length=50,null=False)

	def __str__(self):
		return self.Name


class MSSubAdvs(models.Model):  # model name must NOT the same as column name!
	Name = models.CharField(max_length=730,null=False)

	def __str__(self):
		return self.Name


class MgrNames(models.Model):  # model name must NOT the same as column name!
	Name = models.CharField(max_length=1000,null=False)

	def __str__(self):
		return self.Name


class Company(models.Model):
	Name	= models.CharField(max_length=40)
	CUSIP	= models.CharField(max_length=9,null=True)
	SecId	= models.CharField(max_length=10,null=True)
	FundId	= models.CharField(max_length=10,null=True)
	MRFundID	= models.CharField(max_length=15,null=True)
	PerfID	= models.CharField(max_length=15,null=True)
	Ticker	= models.CharField(max_length=12,null=True)
	OldestSh	= models.CharField(max_length=5,null=True)
	Advisor	= models.CharField(max_length=200,null=True)
	AdvisorID = models.ForeignKey(Advisors, on_delete=models.SET_NULL, null=True)
	FirmName	= models.CharField(max_length=100,null=True)
	BrndName	= models.CharField(max_length=44,null=True)
	BrndNmID	= models.CharField(max_length=10,null=True)
	InceptDt	=models.DateField(null=True)			
	GlBrdGrp	= models.CharField(max_length=13,null=True)
	GlBrdCat	= models.CharField(max_length=39,null=True)
	USCatGrp	= models.CharField(max_length=20,null=True)
	MSCat	= models.CharField(max_length=50,null=True)
	MSCatDbId = models.ForeignKey(MSCats, on_delete=models.SET_NULL, null=True)
	MSCatID	= models.CharField(max_length=10,null=True)
	MSCatStr	=models.DateField(null=True)			
	MSInsCat	= models.CharField(max_length=43,null=True)
	MSRatAll	= models.CharField(max_length=2,null=True)
	MSRat3Y	= models.CharField(max_length=2,null=True)
	MSRat5Y	= models.CharField(max_length=2,null=True)
	MSRat10Y	= models.CharField(max_length=2,null=True)
	EqStyleL	= models.CharField(max_length=12,null=True)
	EqStyleS	= models.CharField(max_length=12,null=True)
	FxStyleL	= models.CharField(max_length=16,null=True)
	MSSubAdv	= models.CharField(max_length=721,null=True)
	MSSubAdvId = models.ForeignKey(MSSubAdvs, on_delete=models.SET_NULL, null=True)
	MSSubFee	= models.CharField(max_length=516,null=True)
	TeamMgd	= models.CharField(max_length=3,null=True)
	MgrHist	= models.CharField(max_length=5000,null=True)
	MgrName	= models.CharField(max_length=1000,null=True)
	MgrNameId = models.ForeignKey(MgrNames, on_delete=models.SET_NULL, null=True)
	MgrTnrAv	=models.DecimalField(max_digits=6,decimal_places=2, null=True)
	MgrTnrLg	=models.DecimalField(max_digits=6,decimal_places=2, null=True)
	PPBnch	= models.CharField(max_length=400,null=True)
	PPBnchID	= models.CharField(max_length=10,null=True)
	PPBIncpt	=models.DateField(null=True)			
	SPBench	= models.CharField(max_length=400,null=True)
	AUMShr	= models.BigIntegerField(null=True)			
	AUMShrDt	=models.DateField(null=True)			
	FSizeCur	= models.BigIntegerField(null=True)			
	FSizeDt	=models.DateField(null=True)			
	hldBondL	=models.IntegerField(null=True)			
	hldBondS	=models.IntegerField(null=True)			
	hldLong	=models.IntegerField(null=True)			
	hldOthrL	=models.IntegerField(null=True)			
	hldOthrS	=models.IntegerField(null=True)			
	hldStckL	=models.IntegerField(null=True)			
	hldStckS	=models.IntegerField(null=True)			
	hldT10	=models.DecimalField(max_digits=10,decimal_places=6,null=True)
	hldofInv	= models.CharField(max_length=3,null=True)
	hldAT10	=models.DecimalField(max_digits=10,decimal_places=6,null=True)
	hldAT10D	=models.DateField(null=True)			
	Yld12M	=models.DecimalField(max_digits=10,decimal_places=6,null=True)
	Yld12MD	=models.DateField(null=True)			
	SECYld	=models.DecimalField(max_digits=10,decimal_places=5,null=True)
	SECYldD	=models.DateField(null=True)			
	DivdCur	=models.DecimalField(max_digits=11,decimal_places=7,null=True)
	DivdCurD	=models.DateField(null=True)			
	DivdNAVC	=models.DecimalField(max_digits=8,decimal_places=4,null=True)
	PortDate	=models.DateField(null=True)			
	VirtClss	= models.CharField(max_length=3,null=True)
	FeeMgt	=models.DecimalField(max_digits=10,decimal_places=3,null=True)
	NExpSAR	=models.DecimalField(max_digits=7,decimal_places=3,null=True)
	NExpSARD	=models.DateField(null=True)			
	ChrgAR	=models.DecimalField(max_digits=6,decimal_places=3,null=True)
	ChrgARD	=models.DateField(null=True)			
	NExpPrs	=models.DecimalField(max_digits=7,decimal_places=3,null=True)
	NExpPrsD	=models.DecimalField(max_digits=7,decimal_places=3,null=True)
	ObjPros	= models.CharField(max_length=30,null=True)
	Fee12b1	=models.DecimalField(max_digits=5,decimal_places=3,null=True)
	TurnRat	=models.DecimalField(max_digits=10,decimal_places=3,null=True)
	TurnRatD	=models.DateField(null=True)			
	CashN	=models.DecimalField(max_digits=11,decimal_places=6,null=True)
	AABondN	=models.DecimalField(max_digits=11,decimal_places=6,null=True)
	AACashN	=models.DecimalField(max_digits=11,decimal_places=6,null=True)
	AAEqN	=models.DecimalField(max_digits=11,decimal_places=6,null=True)
	AANUSBdN	=models.DecimalField(max_digits=11,decimal_places=6,null=True)
	AANUSEqN	=models.DecimalField(max_digits=10,decimal_places=6,null=True)
	AAOthrN	=models.DecimalField(max_digits=10,decimal_places=6,null=True)
	AAUSBdN	=models.DecimalField(max_digits=11,decimal_places=6,null=True)
	AAUSEqN	=models.DecimalField(max_digits=11,decimal_places=6,null=True)
	AAABN	=models.DecimalField(max_digits=8,decimal_places=6,null=True)
	AABondL	=models.DecimalField(max_digits=15,decimal_places=6,null=True)
	AACashL	=models.DecimalField(max_digits=16,decimal_places=6,null=True)
	AAEqL	=models.DecimalField(max_digits=15,decimal_places=6,null=True)
	AANUSBdL	=models.DecimalField(max_digits=10,decimal_places=6,null=True)
	AANUSEqL	=models.DecimalField(max_digits=10,decimal_places=6,null=True)
	AAOthrL	=models.DecimalField(max_digits=15,decimal_places=6,null=True)
	AAUSBdL	=models.DecimalField(max_digits=10,decimal_places=6,null=True)
	AAUSEqL	=models.DecimalField(max_digits=10,decimal_places=6,null=True)
	FoFIH	= models.CharField(max_length=3,null=True)
	Leveragd	= models.CharField(max_length=3,null=True)
	FeederFd	= models.CharField(max_length=3,null=True)
	MasterFd	= models.CharField(max_length=3,null=True)
	MasterN	= models.CharField(max_length=50,null=True)
	MSTRFundID	= models.CharField(max_length=10,null=True)
	Sharia	= models.CharField(max_length=3,null=True)
	Ethical	= models.CharField(max_length=19,null=True)
	ModelFd	= models.CharField(max_length=2,null=True)
	Avail529	= models.CharField(max_length=3,null=True)
	AvailRet	= models.CharField(max_length=3,null=True)
	AvailIns	= models.CharField(max_length=3,null=True)
	TaxMgd	= models.CharField(max_length=3,null=True)
	Contrarn	= models.CharField(max_length=3,null=True)
	BrkAvail	= models.CharField(max_length=4000,null=True)
	EnhIndex	= models.CharField(max_length=3,null=True)
	Indexed	= models.CharField(max_length=3,null=True)
	FoF	= models.CharField(max_length=3,null=True)
	SocCons	= models.CharField(max_length=3,null=True)
	NonDiv	= models.CharField(max_length=3,null=True)
	ClsdAll	= models.CharField(max_length=3,null=True)
	ClsdALLD	=models.DateField(null=True)			
	ClsdNew	= models.CharField(max_length=3,null=True)
	ClsdNewD	=models.DateField(null=True)			
	FeeAccnt	=models.DecimalField(max_digits=13,decimal_places=6,null=True)
	FeeAdmin	=models.DecimalField(max_digits=9,decimal_places=6,null=True)
	FeeAdv	=models.DecimalField(max_digits=9,decimal_places=6,null=True)
	FeeAudit	=models.DecimalField(max_digits=9,decimal_places=6,null=True)
	FeeCust	=models.DecimalField(max_digits=13,decimal_places=6,null=True)
	FeeDistr	=models.DecimalField(max_digits=13,decimal_places=6,null=True)
	FeeIns	=models.DecimalField(max_digits=9,decimal_places=6,null=True)
	FeeLegal	=models.DecimalField(max_digits=9,decimal_places=6,null=True)
	FeeOrg	=models.DecimalField(max_digits=9,decimal_places=6,null=True)
	FeeOthr	=models.DecimalField(max_digits=9,decimal_places=6,null=True)
	FeePerf	=models.DecimalField(max_digits=9,decimal_places=6,null=True)
	FeeProf	=models.DecimalField(max_digits=12,decimal_places=6,null=True)
	FeeReg	=models.DecimalField(max_digits=11,decimal_places=6,null=True)
	FeeShRpt	=models.DecimalField(max_digits=9,decimal_places=6,null=True)
	FeeTA	=models.DecimalField(max_digits=11,decimal_places=6,null=True)
	Domicile	= models.CharField(max_length=15,null=True)
	BaseCurr	= models.CharField(max_length=20,null=True)
	ObsoltD	=models.DateField(null=True)			
	ObsoltTy	= models.CharField(max_length=30,null=True)
	DiscCurr	=models.DecimalField(max_digits=9,decimal_places=6,null=True)
	ShrType	= models.CharField(max_length=15,null=True)
	AABdLR	= models.CharField(max_length=20,null=True)
	AABdL	= models.CharField(max_length=20,null=True)
	AACshLR	= models.CharField(max_length=20,null=True)
	AACBLR	= models.CharField(max_length=20,null=True)
	AAEqLR	= models.CharField(max_length=20,null=True)
	AAxUSBLR	= models.CharField(max_length=20,null=True)
	AAxUSELR	= models.CharField(max_length=20,null=True)
	AAOtLR	= models.CharField(max_length=20,null=True)
	AAPSLR	= models.CharField(max_length=20,null=True)
	AAUSBLR	= models.CharField(max_length=20,null=True)
	AAUSELR	= models.CharField(max_length=20,null=True)

	def __str__(self):
		return self.Name

	# def get_column_names(self):
	# 	return ["Name", "CUSIP", "SecId", "FundId", "Master FundId", "PerformanceId", "Ticker", "Oldest Share Class", "Advisor", "Firm Name", "Branding Name", "Branding Name ID", "Inception Date", "Global Broad Category Group", "Global Category", "US Category Group", "Morningstar Category", "Morningstar Category Id", "Morningstar Category Start Date", "Morningstar Institutional Category", "Morningstar Rating Overall", "Morningstar Rating 3 Yr", "Morningstar Rating 5 Yr", "Morningstar Rating 10 Yr", "Equity Style Box (Long)", "Equity Style Box (Short)", "Fixed Inc Style Box (Long)", "Subadvisor", "Subadvisor Fee Ratio", "Team Managed", "Manager History", "Manager Name", "Manager Tenure (Average)", "Manager Tenure (Longest)", "Primary Prospectus Benchmark", "Primary Prospectus Benchmark Id", "Primary Prospectus Benchmark Inception Date", "Secondary Prospectus Benchmark", "Net Assets - Share Class Base Currency", "Net Assets Date", "Fund Size Base Currency", "Fund Size Date", "# of Bond Holdings (Long)", "# of Bond Holdings (Short)", "# of Holdings (Long)", "# of Other Holdings (Long)", "# of Other Holdings (Short)", "# of Stock Holdings (Long)", "# of Stock Holdings (Short)", "% Asset in Top 10 Holdings", "Holding of an Investment", "Latest % Asset in Top 10 Holdings", "Latest % Asset in Top 10 Holdings Date", "12 Mo Yield", "12 Mo Yield Date", "SEC Yield", "SEC Yield Date", "Latest Dividend Base Currency", "Latest Dividend Date", "Latest Dividend NAV Base Currency", "Portfolio Date", "Virtual Class", "Management Fee", "Semi-Annual Report Net Expense Ratio", "Semi-Annual Report Net Expense Ratio Date", "Annual Report Ongoing Charge", "Annual Report Ongoing Charge Date", "Prospectus Net Expense Ratio", "Prospectus Gross Expense Ratio", "Prospectus Objective", "12b-1 Fee", "Turnover Ratio %", "Turnover Ratio % Date", "Cash % (Net)", "Asset Alloc Bond % (Net)", "Asset Alloc Cash % (Net)", "Asset Alloc Equity % (Net)", "Asset Alloc Non-US Bond % (Net)", "Asset Alloc Non-US Equity % (Net)", "Asset Alloc Other % (Net)", "Asset Alloc US Bond % (Net)", "Asset Alloc US Equity % (Net)", "Asset Backed % (Net)", "Asset Alloc Bond % (Long)", "Asset Alloc Cash % (Long)", "Asset Alloc Equity % (Long)", "Asset Alloc Non-US Bond % (Long)", "Asset Alloc Non-US Equity % (Long)", "Asset Alloc Other % (Long)", "Asset Alloc US Bond % (Long)", "Asset Alloc US Equity % (Long)", "In-House FOF", "Leveraged Fund", "Feeder Fund", "Master Fund", "Master Fund Name", "Master FundId", "Sharia Compliant", "Ethical Issue Strategy Focus", "Model Portfolio Fund", "Available For 529 Only", "Available For Retirement Plan", "Available In Insurance Product", "Tax Managed", "Contrarian", "Brokerage Availability", "Enhanced Index", "Index Fund", "Fund of Funds", "Socially Conscious", "Non Diversified", "Closed to All Inv", "Closed to All Investors Date", "Closed to New Inv", "Closed to New Investors Date", "Accounting Fee", "Administrator Fee", "Advisor Fee", "Auditor Fee", "Custodian Fee", "Distribution Fee", "Insurance Fee", "Legal Fee", "Organization Fee", "Other Fee", "Performance Fee", "Professional Fee", "Registration Fee", "Shareholder Reporting Fee", "Transfer Agency Fee", "Domicile", "Base Currency", "Obsolete Date", "Obsolete Type", "Discount (Current)", "Share Class Type", "Asset Alloc Bond % (Long Rescaled)", "Asset Alloc Bond % (Long)", "Asset Alloc Cash % (Long Rescaled)", "Asset Alloc Conv Bond % (Long Rescaled)", "Asset Alloc Equity % (Long Rescaled)", "Asset Alloc Non-US Bond % (Long Rescaled)", "Asset Alloc Non-US Equity % (Long Rescaled)", "Asset Alloc Other % (Long Rescaled)", "Asset Alloc Pref Stock % (Long Rescaled)", "Asset Alloc US Bond % (Long Rescaled)", "Asset Alloc US Equity % (Long Rescaled)"]


class Shares(models.Model):
	GR_ID	= models.BigIntegerField(null=True)				
	SecId	= models.CharField(max_length=10, null=True)
	FundId	= models.CharField(max_length=10, null=True)
	OldSecID	= models.CharField(max_length=10, null=True)
	OldGRID	= models.BigIntegerField(null=True)
	CUSIP	= models.CharField(max_length=9, null=True)
	MFVA	= models.CharField(max_length=3, null=True)
	Name	= models.CharField(max_length=100, null=True)
	Ticker	= models.CharField(max_length=15, null=True)
	InceptDt	=models.DateField(null=True)
	MSCat	= models.CharField(max_length=50, null=True)
	MSRat3Y	= models.CharField(max_length=2, null=True)
	MSRat5Y	= models.CharField(max_length=2, null=True)
	MSRat10Y	= models.CharField(max_length=2, null=True)
	MSRatAll	= models.CharField(max_length=2, null=True)
	AUMShr	=models.DecimalField(max_digits=21,decimal_places=10, null=True)
	hldofInv	= models.CharField(max_length=3, null=True)		
	OldestSh	= models.CharField(max_length=3, null=True)		
	Yld12MD	=models.DateField(null=True)
	Yld12M	=models.DecimalField(max_digits=12,decimal_places=6, null=True)
	SECYld	=models.DecimalField(max_digits=12,decimal_places=6, null=True)
	SECYldD	=models.DateField(null=True)
	Fee12b1	=models.DecimalField(max_digits=12,decimal_places=6, null=True)
	NExpSAR	=models.DecimalField(max_digits=12,decimal_places=6, null=True)
	NExpSARD	=models.DateField(null=True)
	NExpPrs	=models.DecimalField(max_digits=12,decimal_places=6, null=True)
	NExpPrsD	=models.DecimalField(max_digits=12,decimal_places=6, null=True)
	BrkAvail	= models.CharField(max_length=4000, null=True)		
	MgrName	= models.CharField(max_length=1000, null=True)		
	Bench	= models.CharField(max_length=50, null=True)		
	Bench_ID	= models.CharField(max_length=20, null=True)		
	TR_YTD	=models.DecimalField(max_digits=21,decimal_places=15, null=True)
	TR_3M	=models.DecimalField(max_digits=21,decimal_places=15, null=True)
	TR_6M	=models.DecimalField(max_digits=21,decimal_places=15, null=True)
	TR_9M	=models.DecimalField(max_digits=21,decimal_places=15, null=True)
	TR_1Y	=models.DecimalField(max_digits=21,decimal_places=15, null=True)
	TR_2Y	=models.DecimalField(max_digits=21,decimal_places=15, null=True)
	TR_3Y	=models.DecimalField(max_digits=21,decimal_places=15, null=True)
	TR_4Y	=models.DecimalField(max_digits=21,decimal_places=15, null=True)
	TR_5Y	=models.DecimalField(max_digits=21,decimal_places=15, null=True)
	TR_10Y	=models.DecimalField(max_digits=21,decimal_places=15, null=True)
	TR_15Y	=models.DecimalField(max_digits=21,decimal_places=15, null=True)
	TR_2017	=models.DecimalField(max_digits=21,decimal_places=15, null=True)
	TR_2016	=models.DecimalField(max_digits=21,decimal_places=15, null=True)
	TR_2015	=models.DecimalField(max_digits=21,decimal_places=15, null=True)
	TR_2014	=models.DecimalField(max_digits=21,decimal_places=15, null=True)
	TR_2013	=models.DecimalField(max_digits=21,decimal_places=15, null=True)
	TR_2012	=models.DecimalField(max_digits=21,decimal_places=15, null=True)
	TR_2011	=models.DecimalField(max_digits=21,decimal_places=15, null=True)
	TR_2010	=models.DecimalField(max_digits=21,decimal_places=15, null=True)
	TR_2009	=models.DecimalField(max_digits=21,decimal_places=15, null=True)
	TR_2008	=models.DecimalField(max_digits=21,decimal_places=15, null=True)
	TR_2007	=models.DecimalField(max_digits=21,decimal_places=15, null=True)
	GTR_YTD	=models.DecimalField(max_digits=21,decimal_places=15, null=True)
	GTR_3M	=models.DecimalField(max_digits=21,decimal_places=15, null=True)
	GTR_6M	=models.DecimalField(max_digits=21,decimal_places=15, null=True)
	GTR_9M	=models.DecimalField(max_digits=21,decimal_places=15, null=True)
	GTR_1Y	=models.DecimalField(max_digits=21,decimal_places=15, null=True)
	GTR_2Y	=models.DecimalField(max_digits=21,decimal_places=15, null=True)
	GTR_3Y	=models.DecimalField(max_digits=21,decimal_places=15, null=True)
	GTR_4Y	=models.DecimalField(max_digits=21,decimal_places=15, null=True)
	GTR_5Y	=models.DecimalField(max_digits=21,decimal_places=15, null=True)
	GTR_10Y	=models.DecimalField(max_digits=21,decimal_places=15, null=True)
	GTR_15Y	=models.DecimalField(max_digits=21,decimal_places=15, null=True)
	GTR_2017	=models.DecimalField(max_digits=21,decimal_places=15, null=True)
	GTR_2016	=models.DecimalField(max_digits=21,decimal_places=15, null=True)
	GTR_2015	=models.DecimalField(max_digits=21,decimal_places=15, null=True)
	GTR_2014	=models.DecimalField(max_digits=21,decimal_places=15, null=True)
	GTR_2013	=models.DecimalField(max_digits=21,decimal_places=15, null=True)
	GTR_2012	=models.DecimalField(max_digits=21,decimal_places=15, null=True)
	GTR_2011	=models.DecimalField(max_digits=21,decimal_places=15, null=True)
	GTR_2010	=models.DecimalField(max_digits=21,decimal_places=15, null=True)
	GTR_2009	=models.DecimalField(max_digits=21,decimal_places=15, null=True)
	GTR_2008	=models.DecimalField(max_digits=21,decimal_places=15, null=True)
	GTR_2007	=models.DecimalField(max_digits=21,decimal_places=15, null=True)
	Alpha3	=models.DecimalField(max_digits=21,decimal_places=15, null=True)
	ExRet3	=models.DecimalField(max_digits=21,decimal_places=15, null=True)
	Sharpe3	=models.DecimalField(max_digits=21,decimal_places=15, null=True)
	InfoRat3	=models.DecimalField(max_digits=21,decimal_places=15, null=True)
	Beta3	=models.DecimalField(max_digits=21,decimal_places=15, null=True)
	Stdev3	=models.DecimalField(max_digits=21,decimal_places=15, null=True)
	R23	=models.DecimalField(max_digits=21,decimal_places=15, null=True)
	UpCap3	=models.DecimalField(max_digits=21,decimal_places=11, null=True)
	DnCap3	=models.DecimalField(max_digits=21,decimal_places=11, null=True)
	TrckErr3	=models.DecimalField(max_digits=21,decimal_places=15, null=True)
	FundUp3	=models.DecimalField(max_digits=21,decimal_places=15, null=True)
	FundDn3	=models.DecimalField(max_digits=21,decimal_places=15, null=True)
	BenchUp3	=models.DecimalField(max_digits=21,decimal_places=15, null=True)
	BenchDn3	=models.DecimalField(max_digits=21,decimal_places=15, null=True)
	BatAvg3	=models.DecimalField(max_digits=21,decimal_places=15, null=True)
	OutPNum3	=models.DecimalField(max_digits=10,decimal_places=5, null=True)



class Funds(models.Model):
	GR_ID	= models.BigIntegerField(null=True)				
	FundId	= models.CharField(max_length=10, null=True)		
	SecId	= models.CharField(max_length=10, null=True)
	MSCat	= models.CharField(max_length=50, null=True)
	ProdType	= models.CharField(max_length=50, null=True)
	MFVA	= models.CharField(max_length=5, null=True)
	Fund	= models.CharField(max_length=100, null=True)		
	Advisor	= models.CharField(max_length=200, null=True)		
	VIT	= models.CharField(max_length=3, null=True)		
	MultiSub	= models.CharField(max_length=3, null=True)	
	SubAdv	= models.CharField(max_length=200, null=True)
	SubAdvd	= models.CharField(max_length=3, null=True)
	RealAdv	= models.CharField(max_length=200, null=True)		
	SubSch	= models.CharField(max_length=200, null=True)		
	SubStart	= models.CharField(max_length=200, null=True)		
	SubRate	=models.DecimalField(max_digits=21,decimal_places=11, null=True)
	SubAlloc	=models.DecimalField(max_digits=21,decimal_places=19, null=True)
	MgdVol	= models.CharField(max_length=3, null=True)		
	SmartBet	= models.CharField(max_length=3, null=True)		
	WatchLst	= models.CharField(max_length=3, null=True)		
	InceptDt	=models.DateField(null=True)				
	InceptYr	=models.IntegerField(null=True)				
	MgrName	= models.CharField(max_length=1500, null=True)		
	MgrTenL	=models.DecimalField(max_digits=6,decimal_places=3, null=True)
	MgrTenA	=models.DecimalField(max_digits=6,decimal_places=3, null=True)
	PrBench	= models.CharField(max_length=500, null=True)		
	MgtFee	=models.DecimalField(max_digits=6,decimal_places=3, null=True)
	CashP	=models.DecimalField(max_digits=15,decimal_places=10, null=True)
	TurnRate	=models.DecimalField(max_digits=16,decimal_places=8, null=True)
	EnhIndex	= models.CharField(max_length=3, null=True)		
	Indexed	= models.CharField(max_length=3, null=True)		
	FoF	= models.CharField(max_length=3, null=True)		
	ESG	= models.CharField(max_length=3, null=True)		
	NonDiv	= models.CharField(max_length=3, null=True)		
	CloseAll	= models.CharField(max_length=3, null=True)		
	CloseNew	= models.CharField(max_length=3, null=True)		
	MastFeed	= models.CharField(max_length=3, null=True)		
	Sleeve	= models.CharField(max_length=200, null=True)		
	TeamMgd	= models.CharField(max_length=3, null=True)		
	Bench	= models.CharField(max_length=200, null=True)		
	Bench_ID	= models.CharField(max_length=50, null=True)		
	Yld12M	=models.DecimalField(max_digits=21,decimal_places=15, null=True)
	SECYld	=models.DecimalField(max_digits=12,decimal_places=8, null=True)
	AS201809	=models.DecimalField(max_digits=24,decimal_places=16, null=True)
	AS201712	=models.DecimalField(max_digits=24,decimal_places=16, null=True)
	AS201612	=models.DecimalField(max_digits=24,decimal_places=16, null=True)
	AS201512	=models.DecimalField(max_digits=24,decimal_places=16, null=True)
	AS201412	=models.DecimalField(max_digits=24,decimal_places=16, null=True)
	AS201312	=models.DecimalField(max_digits=24,decimal_places=16, null=True)
	AS201212	=models.DecimalField(max_digits=24,decimal_places=16, null=True)
	AS201112	=models.DecimalField(max_digits=24,decimal_places=16, null=True)
	AS201012	=models.DecimalField(max_digits=24,decimal_places=16, null=True)
	AS200912	=models.DecimalField(max_digits=24,decimal_places=16, null=True)
	AS200812	=models.DecimalField(max_digits=24,decimal_places=16, null=True)
	AS200712	=models.DecimalField(max_digits=24,decimal_places=16, null=True)
	AS200612	=models.DecimalField(max_digits=24,decimal_places=16, null=True)
	AS200512	=models.DecimalField(max_digits=24,decimal_places=16, null=True)
	AS200412	=models.DecimalField(max_digits=24,decimal_places=16, null=True)
	AS200312	=models.DecimalField(max_digits=24,decimal_places=16, null=True)
	NFYTD	=models.DecimalField(max_digits=36,decimal_places=22, null=True)
	NF3M	=models.DecimalField(max_digits=36,decimal_places=22, null=True)
	MF6M	=models.DecimalField(max_digits=36,decimal_places=22, null=True)
	NF1Y	=models.DecimalField(max_digits=36,decimal_places=22, null=True)
	NF2Y	=models.DecimalField(max_digits=36,decimal_places=22, null=True)
	NF3Y	=models.DecimalField(max_digits=36,decimal_places=22, null=True)
	NF4Y	=models.DecimalField(max_digits=36,decimal_places=22, null=True)
	NF5Y	=models.DecimalField(max_digits=36,decimal_places=22, null=True)
	NF10Y	=models.DecimalField(max_digits=36,decimal_places=22, null=True)
	NF15Y	=models.DecimalField(max_digits=36,decimal_places=22, null=True)
	NF2017	=models.DecimalField(max_digits=36,decimal_places=22, null=True)
	NF2016	=models.DecimalField(max_digits=36,decimal_places=22, null=True)
	NF2015	=models.DecimalField(max_digits=36,decimal_places=22, null=True)
	NF2014	=models.DecimalField(max_digits=36,decimal_places=22, null=True)
	NF2013	=models.DecimalField(max_digits=36,decimal_places=22, null=True)
	NF2012	=models.DecimalField(max_digits=36,decimal_places=22, null=True)
	NF2011	=models.DecimalField(max_digits=36,decimal_places=22, null=True)
	NF2010	=models.DecimalField(max_digits=36,decimal_places=22, null=True)
	NF2009	=models.DecimalField(max_digits=36,decimal_places=22, null=True)
	NF2008	=models.DecimalField(max_digits=36,decimal_places=22, null=True)
	NF2007	=models.DecimalField(max_digits=36,decimal_places=22, null=True)
	NF2006	=models.DecimalField(max_digits=36,decimal_places=22, null=True)
	NF2005	=models.DecimalField(max_digits=36,decimal_places=22, null=True)
	NF2004	=models.DecimalField(max_digits=36,decimal_places=22, null=True)
	NF2003	=models.DecimalField(max_digits=36,decimal_places=22, null=True)
	QKYTD	=models.IntegerField(null=True)				
	QK3M	=models.IntegerField(null=True)				
	QK6M	=models.IntegerField(null=True)				
	QK9M	=models.IntegerField(null=True)				
	QK1Y	=models.IntegerField(null=True)				
	QK2Y	=models.IntegerField(null=True)				
	QK3Y	=models.IntegerField(null=True)				
	QK4Y	=models.IntegerField(null=True)				
	QK5Y	=models.IntegerField(null=True)				
	QK10Y	=models.IntegerField(null=True)				
	QK15Y	=models.IntegerField(null=True)				
	QK2017	=models.IntegerField(null=True)				
	QK2016	=models.IntegerField(null=True)				
	QK2015	=models.IntegerField(null=True)				
	QK2014	=models.IntegerField(null=True)				
	QK2013	=models.IntegerField(null=True)				
	QK2012	=models.IntegerField(null=True)				
	QK2011	=models.IntegerField(null=True)				
	QK2010	=models.IntegerField(null=True)				
	QK2009	=models.IntegerField(null=True)				
	QK2008	=models.IntegerField(null=True)				
	QKAlph3	=models.IntegerField(null=True)				
	QKExRt3	=models.IntegerField(null=True)				
	QKShrp3	=models.IntegerField(null=True)				
	QKInfR3	=models.IntegerField(null=True)				
	QKBeta3	=models.IntegerField(null=True)				
	QKStdv3	=models.IntegerField(null=True)				
	QKRsq3	=models.IntegerField(null=True)				
	QKUpS3	=models.IntegerField(null=True)				
	QKDnS3	=models.IntegerField(null=True)				
	QKTrEr3	=models.IntegerField(null=True)				
	QKFUps3	=models.IntegerField(null=True)				
	QKFDns3	=models.IntegerField(null=True)				
	QKBUps3	=models.IntegerField(null=True)				
	QKBDns3	=models.IntegerField(null=True)				
	QKBAvg3	=models.IntegerField(null=True)				
	QKOutp3	=models.IntegerField(null=True)				
	APAUM	=models.DecimalField(max_digits=24,decimal_places=16, null=True)
	AP201809	=models.DecimalField(max_digits=24,decimal_places=16, null=True)
	AP201712	=models.DecimalField(max_digits=24,decimal_places=16, null=True)
	AP201612	=models.DecimalField(max_digits=24,decimal_places=16, null=True)
	AP201512	=models.DecimalField(max_digits=24,decimal_places=16, null=True)
	AP201412	=models.DecimalField(max_digits=24,decimal_places=16, null=True)
	AP201312	=models.DecimalField(max_digits=24,decimal_places=16, null=True)
	AP201212	=models.DecimalField(max_digits=24,decimal_places=16, null=True)
	AP201112	=models.DecimalField(max_digits=24,decimal_places=16, null=True)
	AP201012	=models.DecimalField(max_digits=24,decimal_places=16, null=True)
	AP200912	=models.DecimalField(max_digits=24,decimal_places=16, null=True)
	AP200812	=models.DecimalField(max_digits=24,decimal_places=16, null=True)
	AP200712	=models.DecimalField(max_digits=24,decimal_places=16, null=True)
	AP200612	=models.DecimalField(max_digits=24,decimal_places=16, null=True)
	AP200512	=models.DecimalField(max_digits=24,decimal_places=16, null=True)
	AP200412	=models.DecimalField(max_digits=24,decimal_places=16, null=True)
	AP200312	=models.DecimalField(max_digits=24,decimal_places=16, null=True)
	NFPYTD	=models.DecimalField(max_digits=36,decimal_places=22, null=True)
	NFP3M	=models.DecimalField(max_digits=36,decimal_places=22, null=True)
	NFP6M	=models.DecimalField(max_digits=36,decimal_places=22, null=True)
	NFP1Y	=models.DecimalField(max_digits=36,decimal_places=22, null=True)
	NFP2Y	=models.DecimalField(max_digits=36,decimal_places=22, null=True)
	NFP3Y	=models.DecimalField(max_digits=36,decimal_places=22, null=True)
	NFP4Y	=models.DecimalField(max_digits=36,decimal_places=22, null=True)
	NFP5Y	=models.DecimalField(max_digits=36,decimal_places=22, null=True)
	NFP10Y	=models.DecimalField(max_digits=36,decimal_places=22, null=True)
	NFP15Y	=models.DecimalField(max_digits=36,decimal_places=22, null=True)
	NFP2017	=models.DecimalField(max_digits=36,decimal_places=22, null=True)
	NFP2016	=models.DecimalField(max_digits=36,decimal_places=22, null=True)
	NFP2015	=models.DecimalField(max_digits=36,decimal_places=22, null=True)
	NFP2014	=models.DecimalField(max_digits=36,decimal_places=22, null=True)
	NFP2013	=models.DecimalField(max_digits=36,decimal_places=22, null=True)
	NFP2012	=models.DecimalField(max_digits=36,decimal_places=22, null=True)
	NFP2011	=models.DecimalField(max_digits=36,decimal_places=22, null=True)
	NFP2010	=models.DecimalField(max_digits=36,decimal_places=22, null=True)
	NFP2009	=models.DecimalField(max_digits=36,decimal_places=22, null=True)
	NFP2008	=models.DecimalField(max_digits=36,decimal_places=22, null=True)
	NFP2007	=models.DecimalField(max_digits=36,decimal_places=22, null=True)
	NFP2006	=models.DecimalField(max_digits=36,decimal_places=22, null=True)
	NFP2005	=models.DecimalField(max_digits=36,decimal_places=22, null=True)
	NFP2004	=models.DecimalField(max_digits=36,decimal_places=22, null=True)
	NFP2003	=models.DecimalField(max_digits=36,decimal_places=22, null=True)
	SubAdvP	= models.CharField(max_length=2000, null=True)
	SubAdvdP	= models.CharField(max_length=3, null=True)
	SubSchP	= models.CharField(max_length=2000, null=True)
	SubStrtP	= models.CharField(max_length=2000, null=True)		
	SubRateP	=models.DecimalField(max_digits=30,decimal_places=22, null=True)
	Platform	= models.CharField(max_length=1000, null=True)		
	Platcnt	=models.IntegerField(null=True)
	valgro2	=models.DecimalField(max_digits=36,decimal_places=22, null=True)
	smlrg2	=models.DecimalField(max_digits=36,decimal_places=22, null=True)
	valgro3	=models.DecimalField(max_digits=36,decimal_places=22, null=True)
	smlrg3	=models.DecimalField(max_digits=36,decimal_places=22, null=True)
	valgro5	=models.DecimalField(max_digits=36,decimal_places=22, null=True)
	smlrg5	=models.DecimalField(max_digits=36,decimal_places=22, null=True)
	AdvPar	= models.CharField(max_length=500, null=True)
	SAdvPar	= models.CharField(max_length=500, null=True)
	MandID	=models.BigIntegerField(null=True)
	SubDollr	=models.DecimalField(max_digits=36,decimal_places=22, null=True)


# List-tables for FitDefault
class FitCategorys(models.Model):
	Name = models.CharField(max_length=50,null=False)

	def __str__(self):
		return self.Name


class FitAdvisors(models.Model):
	Name = models.CharField(max_length=200,null=False)

	def __str__(self):
		return self.Name


class FitSubAdvisors(models.Model):
	Name = models.CharField(max_length=200,null=False)

	def __str__(self):
		return self.Name


class FitManagerNames(models.Model):
	Name = models.CharField(max_length=1500,null=False)

	def __str__(self):
		return self.Name


class FitDefault(models.Model):
	Name	= models.CharField(max_length=40)
	Category	= models.CharField(max_length=50, null=True)# Fund.MSCat
	CategoryId	= models.ForeignKey(FitCategorys, on_delete=models.SET_NULL, null=True)
	MFVA	= models.CharField(max_length=5, null=True)		# Fund.MFVA
	SubAdvised	= models.CharField(max_length=3, null=True)	# Fund.SubAdvd
	IndexFund	= models.CharField(max_length=3, null=True)	# Fund.Indexed
	WatchList	= models.CharField(max_length=3, null=True)	# Fund.WatchLst
	VIT	= models.CharField(max_length=3, null=True)			# Fund.VIT
	FundOfFunds	= models.CharField(max_length=3, null=True)	# Fund.FoF
	InceptionDate	=models.DateField(null=True)			# FUnd.InceptDt
	Advisor	= models.CharField(max_length=200, null=True)	# Fund.Advisor
	AdvisorId = models.ForeignKey(FitAdvisors, on_delete=models.SET_NULL, null=True)
	SubAdvisor	= models.CharField(max_length=200, null=True)	# Fund.SubAdv
	SubAdvisorId = models.ForeignKey(FitSubAdvisors, on_delete=models.SET_NULL, null=True)
	AUM	=models.DecimalField(max_digits=24,decimal_places=16, null=True) # Fund.APAUM
	NFYTD	=models.DecimalField(max_digits=36,decimal_places=22, null=True) # Fund.NFYTD
	NF2017	=models.DecimalField(max_digits=36,decimal_places=22, null=True) # Fund.NF2017
	NF2016	=models.DecimalField(max_digits=36,decimal_places=22, null=True) # Fund.NF2016
	TR_YTD	=models.DecimalField(max_digits=21,decimal_places=15, null=True) # Share.TR_YTD
	TR_1Y	=models.DecimalField(max_digits=21,decimal_places=15, null=True) # Share.TR_1Y
	TR_2Y	=models.DecimalField(max_digits=21,decimal_places=15, null=True) # Share.TR_2Y
	TR_3Y	=models.DecimalField(max_digits=21,decimal_places=15, null=True) # Share.TR_3Y
	TR_5Y	=models.DecimalField(max_digits=21,decimal_places=15, null=True) # Share.TR_5Y
	TR_10Y	=models.DecimalField(max_digits=21,decimal_places=15, null=True) # Share.TR_10Y
	SubStart	= models.CharField(max_length=200, null=True)		# Fund.SubStart
	SubSched	= models.CharField(max_length=200, null=True)		# Fund.SubSch
	SubAdvEffRate=models.DecimalField(max_digits=30,decimal_places=22, null=True) # Fund.SubRateP
	SubRate	=models.DecimalField(max_digits=21,decimal_places=11, null=True) # Fund.SubRate
	Alpha	=models.DecimalField(max_digits=21,decimal_places=15, null=True) # Share.Alpha3
	ExcessRet	=models.DecimalField(max_digits=21,decimal_places=15, null=True) # Share.ExRet3
	Sharpe	=models.DecimalField(max_digits=21,decimal_places=15, null=True) # Share.Sharpe3
	InfoRat	=models.DecimalField(max_digits=21,decimal_places=15, null=True) # Share.InfoRat3
	Beta	=models.DecimalField(max_digits=21,decimal_places=15, null=True) # Share.Beta3
	Stdev	=models.DecimalField(max_digits=21,decimal_places=15, null=True) # Share.Stdev3
	R2	=models.DecimalField(max_digits=21,decimal_places=15, null=True)	 # Share.R23
	UpsideCap	=models.DecimalField(max_digits=21,decimal_places=11, null=True) # Share.UpCap
	DownsideCap	=models.DecimalField(max_digits=21,decimal_places=11, null=True) # Share.DnCap3
	TrackingErr	=models.DecimalField(max_digits=21,decimal_places=15, null=True) # Share.TrckErr3
	QRK_YTD	=models.IntegerField(null=True)		# Fund.QKYTD
	QRK_1Y	=models.IntegerField(null=True)		# Fund.QK1Y
	QRK_2Y	=models.IntegerField(null=True)		# Fund.QK2Y
	QRK_3Y	=models.IntegerField(null=True)		# Fund.QK3Y
	QRK_5Y	=models.IntegerField(null=True)		# Fund.QK5Y
	QRK_10Y	=models.IntegerField(null=True)		# Fund.QK10Y
	QRK_15Y	=models.IntegerField(null=True)		# Fund.QK15Y
	QRK_Alpha	=models.IntegerField(null=True)		# Fund.QKAlph3
	QRK_ExcessRet	=models.IntegerField(null=True)	# Fund.QKExRt3
	QRK_Sharpe	=models.IntegerField(null=True)		# Fund.QKShrp3
	QRK_InfoRat	=models.IntegerField(null=True)		# Fund.QKInfR3
	QRK_Beta	=models.IntegerField(null=True)		# Fund.QKBeta3
	QRK_Stdev	=models.IntegerField(null=True)		# Fund.QKStdv3
	QRK_R2	=models.IntegerField(null=True)			# Fund.QKRsq3
	QRK_UpsideCap	=models.IntegerField(null=True)		# Fund.QKUpS3
	QRK_DownsideCap	=models.IntegerField(null=True)		# Fund.QKDnS3
	QRK_TrackingErr	=models.IntegerField(null=True)		# Fund.QKTrEr3
	TeamManaged	= models.CharField(max_length=3, null=True)	# Fund.TeamMgd
	ProspectusNetExpenseRatio=models.DecimalField(max_digits=12,decimal_places=6, null=True) # Share.NExpPrs
	ManagerName	= models.CharField(max_length=1500, null=True)	# Fund.MgrName
	ManagerNameId = models.ForeignKey(FitManagerNames, on_delete=models.SET_NULL, null=True)
	ManagerTenureLongest =models.DecimalField(max_digits=6,decimal_places=3, null=True)	# Fund.MgrTenL
	ManagerTenureAverage =models.DecimalField(max_digits=6,decimal_places=3, null=True)	# Fund.MgrTenA
	Benchmark	= models.CharField(max_length=200, null=True)	# Fund.Bench
	SecId	= models.CharField(max_length=10, null=True)	# Share.SecId
	FundId	= models.CharField(max_length=10, null=True)	# Share.FundId


class SubAdv(models.Model):
	FundId	= models.CharField(max_length=10, null=True)
	Fund	= models.CharField(max_length=100)
	SubAdvisor	= models.CharField(max_length=200, null=True)
	SubAdvisorId = models.ForeignKey(FitSubAdvisors, on_delete=models.SET_NULL, null=True)
	SubAdvisorParent= models.CharField(max_length=200, null=True)
	AdvisorParent	= models.CharField(max_length=100, null=True)
	SubAdvised		= models.CharField(max_length=3, null=True)
	AgrmStart	=models.DateField(null=True)
	AgrmEnd		=models.DateField(null=True)
	SubStart	=models.DateField(null=True)
	SubEnd		=models.DateField(null=True)
	SubAlloc=models.DecimalField(max_digits=12,decimal_places=5, null=True) # TODO: use dec=3, not 5
	SubAUM	=models.DecimalField(max_digits=12,decimal_places=5, null=True)
	FundAUM	=models.DecimalField(max_digits=12,decimal_places=5, null=True)
	EffSub	=models.DecimalField(max_digits=12,decimal_places=5, null=True)
	SubSched3	= models.CharField(max_length=	150, null=True)

