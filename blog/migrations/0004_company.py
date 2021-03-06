# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-15 23:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog', '0003_delete_company'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=40)),
                ('CUSIP', models.CharField(max_length=9, null=True)),
                ('SecId', models.CharField(max_length=10, null=True)),
                ('FundId', models.CharField(max_length=10, null=True)),
                ('MRFundID', models.CharField(max_length=15, null=True)),
                ('PerfID', models.CharField(max_length=15, null=True)),
                ('Ticker', models.CharField(max_length=12, null=True)),
                ('OldestSh', models.CharField(max_length=5, null=True)),
                ('Advisor', models.CharField(max_length=200, null=True)),
                ('FirmName', models.CharField(max_length=100, null=True)),
                ('BrndName', models.CharField(max_length=44, null=True)),
                ('BrndNmID', models.CharField(max_length=10, null=True)),
                ('InceptDt', models.DateField(null=True)),
                ('GlBrdGrp', models.CharField(max_length=13, null=True)),
                ('GlBrdCat', models.CharField(max_length=39, null=True)),
                ('USCatGrp', models.CharField(max_length=20, null=True)),
                ('MSCat', models.CharField(max_length=50, null=True)),
                ('MSCatID', models.CharField(max_length=10, null=True)),
                ('MSCatStr', models.DateField(null=True)),
                ('MSInsCat', models.CharField(max_length=43, null=True)),
                ('MSRatAll', models.CharField(max_length=2, null=True)),
                ('MSRat3Y', models.CharField(max_length=2, null=True)),
                ('MSRat5Y', models.CharField(max_length=2, null=True)),
                ('MSRat10Y', models.CharField(max_length=2, null=True)),
                ('EqStyleL', models.CharField(max_length=12, null=True)),
                ('EqStyleS', models.CharField(max_length=12, null=True)),
                ('FxStyleL', models.CharField(max_length=16, null=True)),
                ('MSSubAdv', models.CharField(max_length=721, null=True)),
                ('MSSubFee', models.CharField(max_length=516, null=True)),
                ('TeamMgd', models.CharField(max_length=3, null=True)),
                ('MgrHist', models.CharField(max_length=5000, null=True)),
                ('MgrName', models.CharField(max_length=1000, null=True)),
                ('MgrTnrAv', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('MgrTnrLg', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('PPBnch', models.CharField(max_length=400, null=True)),
                ('PPBnchID', models.CharField(max_length=10, null=True)),
                ('PPBIncpt', models.DateField(null=True)),
                ('SPBench', models.CharField(max_length=400, null=True)),
                ('AUMShr', models.BigIntegerField(null=True)),
                ('AUMShrDt', models.DateField(null=True)),
                ('FSizeCur', models.BigIntegerField(null=True)),
                ('FSizeDt', models.DateField(null=True)),
                ('hldBondL', models.IntegerField(null=True)),
                ('hldBondS', models.IntegerField(null=True)),
                ('hldLong', models.IntegerField(null=True)),
                ('hldOthrL', models.IntegerField(null=True)),
                ('hldOthrS', models.IntegerField(null=True)),
                ('hldStckL', models.IntegerField(null=True)),
                ('hldStckS', models.IntegerField(null=True)),
                ('hldT10', models.DecimalField(decimal_places=6, max_digits=10, null=True)),
                ('hldofInv', models.CharField(max_length=3, null=True)),
                ('hldAT10', models.DecimalField(decimal_places=6, max_digits=10, null=True)),
                ('hldAT10D', models.DateField(null=True)),
                ('Yld12M', models.DecimalField(decimal_places=6, max_digits=10, null=True)),
                ('Yld12MD', models.DateField(null=True)),
                ('SECYld', models.DecimalField(decimal_places=5, max_digits=10, null=True)),
                ('SECYldD', models.DateField(null=True)),
                ('DivdCur', models.DecimalField(decimal_places=7, max_digits=11, null=True)),
                ('DivdCurD', models.DateField(null=True)),
                ('DivdNAVC', models.DecimalField(decimal_places=4, max_digits=8, null=True)),
                ('PortDate', models.DateField(null=True)),
                ('VirtClss', models.CharField(max_length=3, null=True)),
                ('FeeMgt', models.DecimalField(decimal_places=3, max_digits=10, null=True)),
                ('NExpSAR', models.DecimalField(decimal_places=3, max_digits=7, null=True)),
                ('NExpSARD', models.DateField(null=True)),
                ('ChrgAR', models.DecimalField(decimal_places=3, max_digits=6, null=True)),
                ('ChrgARD', models.DateField(null=True)),
                ('NExpPrs', models.DecimalField(decimal_places=3, max_digits=7, null=True)),
                ('NExpPrsD', models.DecimalField(decimal_places=3, max_digits=7, null=True)),
                ('ObjPros', models.CharField(max_length=30, null=True)),
                ('Fee12b1', models.DecimalField(decimal_places=3, max_digits=5, null=True)),
                ('TurnRat', models.DecimalField(decimal_places=3, max_digits=10, null=True)),
                ('TurnRatD', models.DateField(null=True)),
                ('CashN', models.DecimalField(decimal_places=6, max_digits=11, null=True)),
                ('AABondN', models.DecimalField(decimal_places=6, max_digits=11, null=True)),
                ('AACashN', models.DecimalField(decimal_places=6, max_digits=11, null=True)),
                ('AAEqN', models.DecimalField(decimal_places=6, max_digits=11, null=True)),
                ('AANUSBdN', models.DecimalField(decimal_places=6, max_digits=11, null=True)),
                ('AANUSEqN', models.DecimalField(decimal_places=6, max_digits=10, null=True)),
                ('AAOthrN', models.DecimalField(decimal_places=6, max_digits=10, null=True)),
                ('AAUSBdN', models.DecimalField(decimal_places=6, max_digits=11, null=True)),
                ('AAUSEqN', models.DecimalField(decimal_places=6, max_digits=11, null=True)),
                ('AAABN', models.DecimalField(decimal_places=6, max_digits=8, null=True)),
                ('AABondL', models.DecimalField(decimal_places=6, max_digits=15, null=True)),
                ('AACashL', models.DecimalField(decimal_places=6, max_digits=16, null=True)),
                ('AAEqL', models.DecimalField(decimal_places=6, max_digits=15, null=True)),
                ('AANUSBdL', models.DecimalField(decimal_places=6, max_digits=10, null=True)),
                ('AANUSEqL', models.DecimalField(decimal_places=6, max_digits=10, null=True)),
                ('AAOthrL', models.DecimalField(decimal_places=6, max_digits=15, null=True)),
                ('AAUSBdL', models.DecimalField(decimal_places=6, max_digits=10, null=True)),
                ('AAUSEqL', models.DecimalField(decimal_places=6, max_digits=10, null=True)),
                ('FoFIH', models.CharField(max_length=3, null=True)),
                ('Leveragd', models.CharField(max_length=3, null=True)),
                ('FeederFd', models.CharField(max_length=3, null=True)),
                ('MasterFd', models.CharField(max_length=3, null=True)),
                ('MasterN', models.CharField(max_length=50, null=True)),
                ('MSTRFundID', models.CharField(max_length=10, null=True)),
                ('Sharia', models.CharField(max_length=3, null=True)),
                ('Ethical', models.CharField(max_length=19, null=True)),
                ('ModelFd', models.CharField(max_length=2, null=True)),
                ('Avail529', models.CharField(max_length=3, null=True)),
                ('AvailRet', models.CharField(max_length=3, null=True)),
                ('AvailIns', models.CharField(max_length=3, null=True)),
                ('TaxMgd', models.CharField(max_length=3, null=True)),
                ('Contrarn', models.CharField(max_length=3, null=True)),
                ('BrkAvail', models.CharField(max_length=4000, null=True)),
                ('EnhIndex', models.CharField(max_length=3, null=True)),
                ('Indexed', models.CharField(max_length=3, null=True)),
                ('FoF', models.CharField(max_length=3, null=True)),
                ('SocCons', models.CharField(max_length=3, null=True)),
                ('NonDiv', models.CharField(max_length=3, null=True)),
                ('ClsdAll', models.CharField(max_length=3, null=True)),
                ('ClsdALLD', models.DateField(null=True)),
                ('ClsdNew', models.CharField(max_length=3, null=True)),
                ('ClsdNewD', models.DateField(null=True)),
                ('FeeAccnt', models.DecimalField(decimal_places=6, max_digits=13, null=True)),
                ('FeeAdmin', models.DecimalField(decimal_places=6, max_digits=9, null=True)),
                ('FeeAdv', models.DecimalField(decimal_places=6, max_digits=9, null=True)),
                ('FeeAudit', models.DecimalField(decimal_places=6, max_digits=9, null=True)),
                ('FeeCust', models.DecimalField(decimal_places=6, max_digits=13, null=True)),
                ('FeeDistr', models.DecimalField(decimal_places=6, max_digits=13, null=True)),
                ('FeeIns', models.DecimalField(decimal_places=6, max_digits=9, null=True)),
                ('FeeLegal', models.DecimalField(decimal_places=6, max_digits=9, null=True)),
                ('FeeOrg', models.DecimalField(decimal_places=6, max_digits=9, null=True)),
                ('FeeOthr', models.DecimalField(decimal_places=6, max_digits=9, null=True)),
                ('FeePerf', models.DecimalField(decimal_places=6, max_digits=9, null=True)),
                ('FeeProf', models.DecimalField(decimal_places=6, max_digits=12, null=True)),
                ('FeeReg', models.DecimalField(decimal_places=6, max_digits=11, null=True)),
                ('FeeShRpt', models.DecimalField(decimal_places=6, max_digits=9, null=True)),
                ('FeeTA', models.DecimalField(decimal_places=6, max_digits=11, null=True)),
                ('Domicile', models.CharField(max_length=15, null=True)),
                ('BaseCurr', models.CharField(max_length=20, null=True)),
                ('ObsoltD', models.DateField(null=True)),
                ('ObsoltTy', models.CharField(max_length=30, null=True)),
                ('DiscCurr', models.DecimalField(decimal_places=6, max_digits=9, null=True)),
                ('ShrType', models.CharField(max_length=15, null=True)),
                ('AABdLR', models.CharField(max_length=20, null=True)),
                ('AABdL', models.CharField(max_length=20, null=True)),
                ('AACshLR', models.CharField(max_length=20, null=True)),
                ('AACBLR', models.CharField(max_length=20, null=True)),
                ('AAEqLR', models.CharField(max_length=20, null=True)),
                ('AAxUSBLR', models.CharField(max_length=20, null=True)),
                ('AAxUSELR', models.CharField(max_length=20, null=True)),
                ('AAOtLR', models.CharField(max_length=20, null=True)),
                ('AAPSLR', models.CharField(max_length=20, null=True)),
                ('AAUSBLR', models.CharField(max_length=20, null=True)),
                ('AAUSELR', models.CharField(max_length=20, null=True)),
            ],
        ),
    ]
