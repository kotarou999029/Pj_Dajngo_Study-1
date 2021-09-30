# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class MClndr(models.Model):
    clndr_dt = models.DateField(db_column='CLNDR_DT', blank=True, null=True)  # Field name made lowercase.
    pj_no = models.CharField(db_column='PJ_NO', max_length=8, blank=True, null=True)  # Field name made lowercase.
    wrk_dt_kbn = models.CharField(db_column='WRK_DT_KBN', max_length=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'M_CLNDR'


class MPjKnr(models.Model):
    pj_no = models.TextField(db_column='PJ_NO', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pj_nm = models.TextField(db_column='PJ_NM', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pj_st_time = models.DateField(db_column='PJ_ST_TIME', blank=True, null=True)  # Field name made lowercase.
    rst_st_time = models.DateField(db_column='RST_ST_TIME', blank=True, null=True)  # Field name made lowercase.
    rst_ed_time = models.DateField(db_column='RST_ED_TIME', blank=True, null=True)  # Field name made lowercase.
    pj_ed_time = models.DateField(db_column='PJ_ED_TIME', blank=True, null=True)  # Field name made lowercase.
    act_hrs = models.TextField(db_column='ACT_HRS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'M_PJ_KNR'


class MPjSzk(models.Model):
    syn_cd = models.CharField(db_column='SYN_CD', max_length=6, blank=True, null=True)  # Field name made lowercase.
    pj_kbn = models.CharField(db_column='PJ_KBN', max_length=2, blank=True, null=True)  # Field name made lowercase.
    pj_no = models.CharField(db_column='PJ_NO', max_length=8, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'M_PJ_SZK'


class MUsr(models.Model):
    syn_cd = models.CharField(db_column='SYN_CD', max_length=6, blank=True, null=True)  # Field name made lowercase.
    syn_nm_s_kj = models.TextField(db_column='SYN_NM_S_KJ', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    syn_nm_n_kj = models.TextField(db_column='SYN_NM_N_KJ', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    syn_nm_s_kn = models.TextField(db_column='SYN_NM_S_KN', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    syn_nm_n_kn = models.TextField(db_column='SYN_NM_N_KN', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    nysy_dt = models.DateField(db_column='NYSY_DT', blank=True, null=True)  # Field name made lowercase.
    pj_add_dt = models.DateField(db_column='PJ_ADD_DT', blank=True, null=True)  # Field name made lowercase.
    pj_del_dt = models.DateField(db_column='PJ_DEL_DT', blank=True, null=True)  # Field name made lowercase.
    e_mail_adr = models.TextField(db_column='E_MAIL_ADR', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    syn_kngn = models.CharField(db_column='SYN_KNGN', max_length=2, blank=True, null=True)  # Field name made lowercase.
    lgn_pss = models.TextField(db_column='LGN_PSS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    syn_kbn = models.CharField(db_column='SYN_KBN', max_length=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'M_USR'


class TKnti(models.Model):
    syn_cd = models.CharField(db_column='SYN_CD', max_length=6, blank=True, null=True)  # Field name made lowercase.
    knti_dt = models.DateField(db_column='KNTI_DT', blank=True, null=True)  # Field name made lowercase.
    ido_kbn = models.CharField(db_column='IDO_KBN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    pj_no = models.TextField(db_column='PJ_NO', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    rmrks = models.TextField(db_column='RMRKS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'T_KNTI'


class TKntiDtl(models.Model):
    syn_cd = models.CharField(db_column='SYN_CD', max_length=6, blank=True, null=True)  # Field name made lowercase.
    knti_dt = models.DateField(db_column='KNTI_DT', blank=True, null=True)  # Field name made lowercase.
    pj_no = models.CharField(db_column='PJ_NO', max_length=8, blank=True, null=True)  # Field name made lowercase.
    wrk_st_time = models.DateField(db_column='WRK_ST_TIME', blank=True, null=True)  # Field name made lowercase.
    wrk_ed_time = models.DateField(db_column='WRK_ED_TIME', blank=True, null=True)  # Field name made lowercase.
    act_hrs = models.TextField(db_column='ACT_HRS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    rst_hrs = models.TextField(db_column='RST_HRS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    mdnght_wrk_hrs = models.TextField(db_column='MDNGHT_WRK_HRS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    nn_rglr_wrk_hrs = models.TextField(db_column='NN_RGLR_WRK_HRS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'T_KNTI_DTL'

