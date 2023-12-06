# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class ElsiCollegeDtls(models.Model):
    id = models.IntegerField(blank=True, null=True)
    clg_code = models.TextField(blank=True, null=True)
    region_id = models.IntegerField(blank=True, null=True)
    workshop_id = models.IntegerField(blank=True, null=True)
    college_name = models.TextField(blank=True, null=True)
    abbreviation = models.TextField(blank=True, null=True)
    district = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    state = models.TextField(blank=True, null=True)
    pincode = models.IntegerField(blank=True, null=True)
    college_type = models.TextField(blank=True, null=True)
    principal_meet = models.IntegerField(blank=True, null=True)
    robots_given = models.IntegerField(blank=True, null=True)
    eyic_allowed = models.TextField(blank=True, null=True)
    eyrtc_allowed = models.IntegerField(blank=True, null=True)
    tbt_allowed = models.IntegerField(blank=True, null=True)
    content_allowed = models.TextField(blank=True, null=True)
    legal_docs = models.TextField(blank=True, null=True)
    legal_docs_remarks = models.TextField(blank=True, null=True)
    loi_status = models.IntegerField(blank=True, null=True)
    loi_format = models.IntegerField(blank=True, null=True)
    loi_remarks = models.TextField(blank=True, null=True)
    po_status = models.TextField(blank=True, null=True)
    po_remark = models.TextField(blank=True, null=True)
    wo_reg = models.TextField(blank=True, null=True)
    wo_invite = models.TextField(blank=True, null=True)
    wo_confirm = models.TextField(blank=True, null=True)
    wo_attend = models.IntegerField(blank=True, null=True)
    hardware_given = models.TextField(blank=True, null=True)
    lab_inaugurated = models.IntegerField(blank=True, null=True)
    phase = models.TextField(blank=True, null=True)
    eys2016_invites = models.TextField(blank=True, null=True)
    team_verify = models.IntegerField(blank=True, null=True)
    created_at = models.TextField(blank=True, null=True)
    updated_at = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'elsi_college_dtls'


class ElsiCompetitions(models.Model):
    id = models.IntegerField(blank=True, null=True)
    year = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    theme = models.TextField(blank=True, null=True)
    phase = models.IntegerField(blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    created_at = models.TextField(blank=True, null=True)
    updated_at = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'elsi_competitions'


class ElsiDepartments(models.Model):
    id = models.IntegerField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    main_branch = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'elsi_departments'


class ElsiDesignations(models.Model):
    id = models.IntegerField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'elsi_designations'


class ElsiState(models.Model):
    id = models.IntegerField(blank=True, null=True)
    code = models.TextField(blank=True, null=True)
    state = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'elsi_state'


class ElsiTeacherDtls(models.Model):
    id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    clg_id = models.IntegerField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    emailid = models.TextField(blank=True, null=True)
    alt_email1 = models.TextField(blank=True, null=True)
    alt_email2 = models.TextField(blank=True, null=True)
    contact_num = models.TextField(blank=True, null=True)
    alt_contact1 = models.TextField(blank=True, null=True)
    department = models.TextField(blank=True, null=True)
    designation = models.TextField(blank=True, null=True)
    gender = models.TextField(blank=True, null=True)
    coor_flag = models.IntegerField(blank=True, null=True)
    wo_flag = models.IntegerField(blank=True, null=True)
    workshop_id = models.IntegerField(blank=True, null=True)
    wo_attendee = models.IntegerField(blank=True, null=True)
    wo_count = models.IntegerField(blank=True, null=True)
    eyrtc_flag = models.IntegerField(blank=True, null=True)
    tbt_flag = models.IntegerField(blank=True, null=True)
    eyic_flag = models.TextField(blank=True, null=True)
    content_flag = models.TextField(blank=True, null=True)
    status = models.TextField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    status_flag = models.TextField(blank=True, null=True)
    modified_by = models.TextField(blank=True, null=True)
    elsi_flag = models.TextField(blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    login_created = models.TextField(blank=True, null=True)
    created_at = models.TextField(blank=True, null=True)
    updated_at = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'elsi_teacher_dtls'


class MainClgdata(models.Model):
    cname = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'main_clgdata'


class MainLocdata(models.Model):
    locstate = models.CharField(max_length=50)
    locdistrict = models.CharField(max_length=50)
    locemail = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'main_locdata'


class WorkshopDtls(models.Model):
    id = models.IntegerField(blank=True, null=True)
    region_id = models.IntegerField(blank=True, null=True)
    clg_id = models.IntegerField(blank=True, null=True)
    active = models.TextField(blank=True, null=True)
    workshop_team = models.TextField(blank=True, null=True)
    start_date = models.TextField(blank=True, null=True)
    end_date = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'workshop_dtls'


class WorkshopParticipants(models.Model):
    id = models.IntegerField(blank=True, null=True)
    workshop_id = models.IntegerField(blank=True, null=True)
    clg_id = models.IntegerField(blank=True, null=True)
    tch_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'workshop_participants'
