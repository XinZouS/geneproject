# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-15 23:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='AAABN',
            field=models.DecimalField(decimal_places=6, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='AABdL',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='AABdLR',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='AABondL',
            field=models.DecimalField(decimal_places=6, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='AABondN',
            field=models.DecimalField(decimal_places=6, max_digits=11, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='AACBLR',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='AACashL',
            field=models.DecimalField(decimal_places=6, max_digits=16, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='AACashN',
            field=models.DecimalField(decimal_places=6, max_digits=11, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='AACshLR',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='AAEqL',
            field=models.DecimalField(decimal_places=6, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='AAEqLR',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='AAEqN',
            field=models.DecimalField(decimal_places=6, max_digits=11, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='AANUSBdL',
            field=models.DecimalField(decimal_places=6, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='AANUSBdN',
            field=models.DecimalField(decimal_places=6, max_digits=11, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='AANUSEqL',
            field=models.DecimalField(decimal_places=6, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='AANUSEqN',
            field=models.DecimalField(decimal_places=6, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='AAOtLR',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='AAOthrL',
            field=models.DecimalField(decimal_places=6, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='AAOthrN',
            field=models.DecimalField(decimal_places=6, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='AAPSLR',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='AAUSBLR',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='AAUSBdL',
            field=models.DecimalField(decimal_places=6, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='AAUSBdN',
            field=models.DecimalField(decimal_places=6, max_digits=11, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='AAUSELR',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='AAUSEqL',
            field=models.DecimalField(decimal_places=6, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='AAUSEqN',
            field=models.DecimalField(decimal_places=6, max_digits=11, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='AAxUSBLR',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='AAxUSELR',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='AUMShr',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='AUMShrDt',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='Advisor',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='Avail529',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='AvailIns',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='AvailRet',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='BaseCurr',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='BrkAvail',
            field=models.CharField(max_length=4000, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='BrndName',
            field=models.CharField(max_length=44, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='BrndNmID',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='CUSIP',
            field=models.CharField(max_length=9, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='CashN',
            field=models.DecimalField(decimal_places=6, max_digits=11, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='ChrgAR',
            field=models.DecimalField(decimal_places=3, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='ChrgARD',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='ClsdALLD',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='ClsdAll',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='ClsdNew',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='ClsdNewD',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='Contrarn',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='DiscCurr',
            field=models.DecimalField(decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='DivdCur',
            field=models.DecimalField(decimal_places=7, max_digits=11, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='DivdCurD',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='DivdNAVC',
            field=models.DecimalField(decimal_places=4, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='Domicile',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='EnhIndex',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='EqStyleL',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='EqStyleS',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='Ethical',
            field=models.CharField(max_length=19, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='FSizeCur',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='FSizeDt',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='Fee12b1',
            field=models.DecimalField(decimal_places=3, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='FeeAccnt',
            field=models.DecimalField(decimal_places=6, max_digits=13, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='FeeAdmin',
            field=models.DecimalField(decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='FeeAdv',
            field=models.DecimalField(decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='FeeAudit',
            field=models.DecimalField(decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='FeeCust',
            field=models.DecimalField(decimal_places=6, max_digits=13, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='FeeDistr',
            field=models.DecimalField(decimal_places=6, max_digits=13, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='FeeIns',
            field=models.DecimalField(decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='FeeLegal',
            field=models.DecimalField(decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='FeeMgt',
            field=models.DecimalField(decimal_places=3, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='FeeOrg',
            field=models.DecimalField(decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='FeeOthr',
            field=models.DecimalField(decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='FeePerf',
            field=models.DecimalField(decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='FeeProf',
            field=models.DecimalField(decimal_places=6, max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='FeeReg',
            field=models.DecimalField(decimal_places=6, max_digits=11, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='FeeShRpt',
            field=models.DecimalField(decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='FeeTA',
            field=models.DecimalField(decimal_places=6, max_digits=11, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='FeederFd',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='FirmName',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='FoF',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='FoFIH',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='FundId',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='FxStyleL',
            field=models.CharField(max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='GlBrdCat',
            field=models.CharField(max_length=39, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='GlBrdGrp',
            field=models.CharField(max_length=13, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='InceptDt',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='Indexed',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='Leveragd',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='MRFundID',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='MSCat',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='MSCatID',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='MSCatStr',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='MSInsCat',
            field=models.CharField(max_length=43, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='MSRat10Y',
            field=models.CharField(max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='MSRat3Y',
            field=models.CharField(max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='MSRat5Y',
            field=models.CharField(max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='MSRatAll',
            field=models.CharField(max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='MSSubAdv',
            field=models.CharField(max_length=721, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='MSSubFee',
            field=models.CharField(max_length=516, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='MSTRFundID',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='MasterFd',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='MasterN',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='MgrHist',
            field=models.CharField(max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='MgrName',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='MgrTnrAv',
            field=models.DecimalField(decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='MgrTnrLg',
            field=models.DecimalField(decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='ModelFd',
            field=models.CharField(max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='NExpPrs',
            field=models.DecimalField(decimal_places=3, max_digits=7, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='NExpPrsD',
            field=models.DecimalField(decimal_places=3, max_digits=7, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='NExpSAR',
            field=models.DecimalField(decimal_places=3, max_digits=7, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='NExpSARD',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='NonDiv',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='ObjPros',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='ObsoltD',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='ObsoltTy',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='OldestSh',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='PPBIncpt',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='PPBnch',
            field=models.CharField(max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='PPBnchID',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='PerfID',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='PortDate',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='SECYld',
            field=models.DecimalField(decimal_places=5, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='SECYldD',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='SPBench',
            field=models.CharField(max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='SecId',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='Sharia',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='ShrType',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='SocCons',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='TaxMgd',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='TeamMgd',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='Ticker',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='TurnRat',
            field=models.DecimalField(decimal_places=3, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='TurnRatD',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='USCatGrp',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='VirtClss',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='Yld12M',
            field=models.DecimalField(decimal_places=6, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='Yld12MD',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='hldAT10',
            field=models.DecimalField(decimal_places=6, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='hldAT10D',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='hldBondL',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='hldBondS',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='hldLong',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='hldOthrL',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='hldOthrS',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='hldStckL',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='hldStckS',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='hldT10',
            field=models.DecimalField(decimal_places=6, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='hldofInv',
            field=models.CharField(max_length=3, null=True),
        ),
    ]
