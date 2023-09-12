# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Table51(models.Model):
    pincode = models.IntegerField(primary_key=True)
    first_500_gm = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    every_500_gm = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    turn_around_days = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TABLE 51'


class Adanalytics(models.Model):
    analytics_id = models.AutoField(primary_key=True)
    ad_id = models.IntegerField()
    no_of_hits = models.IntegerField()
    no_of_impression = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'adanalytics'


class Adpages(models.Model):
    adpage_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=225)
    action_name = models.CharField(max_length=225)
    controller_name = models.CharField(max_length=225)

    class Meta:
        managed = False
        db_table = 'adpages'


class Ads(models.Model):
    ad_id = models.AutoField(primary_key=True)
    ad_type = models.CharField(max_length=1)
    page = models.CharField(max_length=225)
    location = models.CharField(max_length=225)
    adword_text = models.TextField(blank=True, null=True)
    title = models.CharField(max_length=225, blank=True, null=True)
    url = models.TextField(blank=True, null=True)
    image = models.CharField(max_length=225, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    is_active = models.CharField(max_length=1)
    i_by = models.IntegerField()
    i_date = models.IntegerField()
    u_by = models.IntegerField()
    u_date = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ads'


class Affiliate(models.Model):
    affiliate_id = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=100)
    user_email = models.CharField(max_length=2000)
    product_title = models.CharField(max_length=1000)
    mypustak_price = models.CharField(max_length=1000)
    mypustak_availibility = models.CharField(max_length=1000)
    affiliate_name = models.CharField(max_length=1000)
    affiliate_url = models.CharField(max_length=5000)
    affiliate_title = models.CharField(max_length=2000)
    affiliate_price = models.CharField(max_length=1000)
    affiliate_availibility = models.CharField(max_length=1000)
    affiliate_condition = models.CharField(max_length=1000)
    timestamp = models.DateTimeField()
    cashback_status = models.CharField(max_length=1000)
    cashback_amount = models.CharField(max_length=1000)

    class Meta:
        managed = False
        db_table = 'affiliate'


class ApiLogs(models.Model):
    sno = models.BigAutoField(primary_key=True)
    api_type = models.CharField(max_length=20, blank=True, null=True)
    api_url = models.CharField(max_length=350, blank=True, null=True)
    api_url_type = models.CharField(max_length=20, blank=True, null=True)
    api_request_params = models.TextField(blank=True, null=True)
    api_response = models.TextField(blank=True, null=True)
    api_request_time = models.DateTimeField(blank=True, null=True)
    api_response_time = models.DateTimeField(blank=True, null=True)
    api_response_duration = models.IntegerField(blank=True, null=True)
    order_id = models.BigIntegerField(blank=True, null=True)
    valid_upto = models.DateTimeField(blank=True, null=True)
    is_valid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'api_logs'


class AramexCod(models.Model):
    pincode = models.IntegerField(primary_key=True)
    first_500_gm = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    every_500_gm = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    turn_around_time = models.CharField(max_length=6, blank=True, null=True)
    cod_charges = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aramex_cod'


class AramexPrepaid(models.Model):
    pincode = models.IntegerField(primary_key=True)
    first_500_gm = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    every_500_gm = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    turn_around_days = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aramex_prepaid'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

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
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
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


class BannerSettings(models.Model):
    banner_setting_id = models.AutoField(primary_key=True)
    banner_type = models.CharField(max_length=1)
    spinner = models.CharField(max_length=255)
    timer = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'banner_settings'


class Banners(models.Model):
    banner_id = models.AutoField(primary_key=True)
    banner_text = models.TextField()
    banner_image = models.CharField(max_length=225)
    banner_button_text = models.CharField(max_length=225)
    banner_button_url = models.CharField(max_length=225)
    banner_order = models.IntegerField()
    type = models.CharField(max_length=1)
    category = models.IntegerField()
    is_active = models.CharField(max_length=1)
    is_deleted = models.CharField(max_length=1)
    i_by = models.IntegerField()
    i_date = models.IntegerField()
    u_by = models.IntegerField()
    u_date = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'banners'


class BookfairSubscription(models.Model):
    bookfair_subscription_id = models.AutoField(primary_key=True)
    bookfair_email = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'bookfair_subscription'


class Bookinventory(models.Model):
    book_inv_id = models.AutoField(primary_key=True)
    book_id = models.IntegerField()
    rack_no = models.CharField(max_length=225)
    donation_req_id = models.IntegerField()
    book_condition = models.CharField(max_length=225, blank=True, null=True)
    handling_charge = models.CharField(max_length=255, blank=True, null=True)
    new_shipping = models.CharField(max_length=255, blank=True, null=True)
    new_handling = models.CharField(max_length=255, blank=True, null=True)
    is_approved = models.CharField(max_length=1)
    is_soldout = models.CharField(max_length=1)
    is_deleted = models.CharField(max_length=1)
    i_by = models.IntegerField()
    i_date = models.IntegerField()
    u_by = models.IntegerField()
    u_date = models.IntegerField()
    uploaded_by = models.CharField(max_length=255)
    actual_date_upload = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bookinventory'


class Booknotify(models.Model):
    bookid = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField()
    book_name = models.CharField(max_length=255, blank=True, null=True)
    isbn = models.IntegerField(blank=True, null=True)
    is_mail_sent = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'booknotify'


class Books(models.Model):
    book_id = models.AutoField(primary_key=True)
    sku = models.CharField(max_length=225)
    isbn = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, blank=True, null=True)
    thumb = models.CharField(max_length=225)
    author = models.CharField(max_length=255, blank=True, null=True)
    publication = models.CharField(max_length=225, blank=True, null=True)
    category = models.IntegerField()
    publication_date = models.IntegerField(blank=True, null=True)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    weight = models.CharField(max_length=225, blank=True, null=True)
    binding = models.CharField(max_length=225, blank=True, null=True)
    edition = models.CharField(max_length=225, blank=True, null=True)
    shipping_cost = models.FloatField()
    book_desc = models.TextField(blank=True, null=True)
    book_desc_url = models.CharField(max_length=255, blank=True, null=True)
    no_of_pages = models.CharField(max_length=225, blank=True, null=True)
    language = models.CharField(max_length=225, blank=True, null=True)
    is_allow_multi_order = models.CharField(max_length=1)
    qty = models.IntegerField()
    published = models.CharField(max_length=1)
    is_cashondelivery = models.CharField(max_length=1)
    is_featured = models.CharField(max_length=1)
    is_publication_house = models.CharField(max_length=1)
    is_out_of_stack = models.CharField(max_length=1)
    is_deleted = models.CharField(max_length=1)
    is_doubtful = models.CharField(max_length=1)
    keywords = models.TextField(blank=True, null=True)
    i_by = models.IntegerField()
    i_date = models.IntegerField()
    u_by = models.IntegerField()
    u_date = models.IntegerField()
    uploaded_by = models.CharField(max_length=255, blank=True, null=True)
    actual_date_upload = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'books'


class CartSession(models.Model):
    cart_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    book_id = models.IntegerField()
    times = models.DateTimeField()
    book_puchased = models.CharField(max_length=1)
    is_mail_sent = models.CharField(max_length=10)
    is_deleted = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cart_session'


class Categories(models.Model):
    parent_id = models.IntegerField(blank=True, null=True)
    lft = models.IntegerField(blank=True, null=True)
    rght = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    slug = models.CharField(max_length=255, blank=True, null=True)
    category_image = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.CharField(max_length=1)
    book_count = models.IntegerField(blank=True, null=True)
    is_deleted = models.CharField(max_length=1)
    i_by = models.IntegerField(blank=True, null=True)
    i_date = models.IntegerField(blank=True, null=True)
    u_by = models.IntegerField(blank=True, null=True)
    u_date = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categories'


class Cities(models.Model):
    city_id = models.AutoField(primary_key=True)
    state_id = models.IntegerField()
    city = models.CharField(max_length=255)
    is_active = models.CharField(max_length=1)
    is_deleted = models.CharField(max_length=1)
    i_by = models.IntegerField()
    i_date = models.IntegerField()
    u_by = models.IntegerField()
    u_date = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cities'


class Cms(models.Model):
    cms_id = models.AutoField(primary_key=True)
    page_name = models.CharField(max_length=225)
    page_title = models.CharField(max_length=225)
    page_desc = models.TextField()
    seo_keyword = models.CharField(max_length=225)
    seo_desc = models.CharField(max_length=225)
    seo_url = models.CharField(max_length=225)
    is_deleted = models.CharField(max_length=1)
    is_active = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cms'


class CodExotel(models.Model):
    order_id = models.IntegerField()
    phone = models.CharField(max_length=50)
    attempts = models.IntegerField()
    i_date = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cod_exotel'


class Countries(models.Model):
    country = models.CharField(max_length=255)
    code = models.CharField(max_length=10)
    is_active = models.CharField(max_length=1, blank=True, null=True)
    is_deleted = models.CharField(max_length=1, blank=True, null=True)
    i_by = models.IntegerField()
    i_date = models.IntegerField()
    u_by = models.IntegerField()
    u_date = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'countries'


class Coupon(models.Model):
    code = models.CharField(max_length=255)
    description = models.CharField(max_length=1000, blank=True, null=True)
    is_active = models.IntegerField()
    is_multiple = models.IntegerField()
    coupon_limit = models.IntegerField()
    type = models.IntegerField()
    type_value = models.IntegerField()
    valid_from = models.CharField(max_length=50, blank=True, null=True)
    valid_to = models.CharField(max_length=50)
    min_cart_val = models.IntegerField()
    is_deleted = models.CharField(max_length=1)
    i_by = models.IntegerField()
    i_date = models.IntegerField()
    u_by = models.IntegerField()
    u_date = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'coupon'


class Dec161609(models.Model):
    order_id = models.IntegerField()
    book_id = models.IntegerField()
    handling_charge = models.CharField(max_length=255)
    price = models.FloatField()
    shipping_cost = models.FloatField()
    weight = models.CharField(max_length=225, blank=True, null=True)
    status = models.IntegerField()
    no_of_book = models.IntegerField()
    cod_charge = models.CharField(max_length=255, blank=True, null=True)
    coupon_amount = models.IntegerField()
    publication_date = models.IntegerField(blank=True, null=True)
    category = models.IntegerField()
    book_uploaded_date = models.DateField(blank=True, null=True)
    order_created_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dec16_1609'


class Delhivery(models.Model):
    pincode = models.IntegerField(primary_key=True)
    first_kg = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    second_kg = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    turn_around_days = models.IntegerField(blank=True, null=True)
    cod_charge = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'delhivery'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
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


class DonationBook(models.Model):
    id = models.IntegerField(primary_key=True)
    donation_req_id = models.IntegerField()
    book_id_from = models.IntegerField()
    book_id_to = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'donation_book'


class DonationTracking(models.Model):
    donation_tracking_id = models.AutoField(primary_key=True)
    donation_req_id = models.IntegerField()
    tracking_no = models.CharField(unique=True, max_length=255)
    warehouse = models.CharField(max_length=255)
    from_barcode = models.IntegerField(blank=True, null=True)
    to_barcode = models.IntegerField(blank=True, null=True)
    study_material = models.IntegerField(blank=True, null=True)
    book_wastage = models.IntegerField(blank=True, null=True)
    is_received = models.CharField(max_length=11, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'donation_tracking'


class Donationreqbooks(models.Model):
    donation_req_book_id = models.AutoField(primary_key=True)
    donationreq_id = models.IntegerField()
    title = models.CharField(max_length=225)
    category = models.IntegerField()
    author = models.CharField(max_length=225)
    publication = models.CharField(max_length=225)

    class Meta:
        managed = False
        db_table = 'donationreqbooks'


class Donationreqs(models.Model):
    donation_req_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    volunteer_id = models.IntegerField(blank=True, null=True)
    track_url = models.CharField(max_length=225, blank=True, null=True)
    declaration_form = models.CharField(max_length=225, blank=True, null=True)
    awb_attachment = models.CharField(max_length=225, blank=True, null=True)
    status = models.IntegerField()
    mobile = models.CharField(db_column='Mobile', max_length=100, blank=True, null=True)  # Field name made lowercase.
    address = models.TextField()
    landmark = models.CharField(db_column='Landmark', max_length=225, blank=True, null=True)  # Field name made lowercase.
    country = models.IntegerField()
    state = models.IntegerField()
    city = models.CharField(max_length=225)
    zipcode = models.CharField(max_length=10)
    no_of_book = models.IntegerField()
    no_of_cartons = models.IntegerField()
    app_books_weight = models.IntegerField()
    donated_book_category = models.CharField(max_length=255)
    pickup_date_time = models.IntegerField()
    donation_image = models.CharField(max_length=225, blank=True, null=True)
    how_do_u_know_abt_us = models.CharField(max_length=225)
    wastage = models.IntegerField()
    document_mail_sent = models.CharField(max_length=1)
    is_blocked = models.CharField(max_length=1)
    i_date = models.IntegerField()
    u_date = models.IntegerField(blank=True, null=True)
    tracking_no = models.CharField(max_length=255, blank=True, null=True)
    is_paid_donation = models.CharField(max_length=1)
    payment_url = models.CharField(max_length=255, blank=True, null=True)
    payment_id = models.CharField(max_length=255, blank=True, null=True)
    donor_name = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'donationreqs'


class DonationresNotes(models.Model):
    donationreq_note_id = models.AutoField(primary_key=True)
    donationreq_id = models.IntegerField()
    note = models.TextField()
    i_by = models.IntegerField()
    i_date = models.IntegerField()
    u_by = models.IntegerField()
    u_date = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'donationres_notes'


class ExotelResponse(models.Model):
    order_id = models.IntegerField()
    phone_no = models.IntegerField()
    customer_response = models.CharField(max_length=255)
    call_sid = models.CharField(max_length=255, blank=True, null=True)
    call_details = models.CharField(max_length=10000)
    i_date = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'exotel_response'


class FaqUserComment(models.Model):
    faqcat_id = models.IntegerField()
    faq_id = models.IntegerField()
    user_id = models.IntegerField()
    title = models.CharField(max_length=255)
    comment = models.TextField()
    i_date = models.IntegerField()
    u_date = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'faq_user_comment'


class Faqcategories(models.Model):
    faqcat_id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=225)
    is_active = models.CharField(max_length=1)
    is_deleted = models.CharField(max_length=1)
    i_by = models.IntegerField()
    i_date = models.IntegerField()
    u_by = models.IntegerField()
    u_date = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'faqcategories'


class Faqs(models.Model):
    faq_id = models.AutoField(primary_key=True)
    faqcat_id = models.IntegerField()
    question = models.CharField(max_length=225)
    answer = models.TextField()
    is_active = models.CharField(max_length=1)
    is_deleted = models.CharField(max_length=1)
    i_by = models.IntegerField()
    i_date = models.IntegerField()
    u_by = models.IntegerField()
    u_date = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'faqs'


class FedexCod(models.Model):
    pincode = models.IntegerField(primary_key=True)
    first_kg = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    second_kg = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    every_additional_kg = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    cod_charge = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fedex_cod'


class FedexPrepaid(models.Model):
    pincode = models.IntegerField(primary_key=True)
    first_kg = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    second_kg = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    additional_1_kg = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fedex_prepaid'


class Messages(models.Model):
    msg_id = models.AutoField(primary_key=True)
    from_field = models.IntegerField(db_column='from')  # Field renamed because it was a Python reserved word.
    to = models.TextField()
    subject = models.CharField(max_length=225)
    message = models.TextField()
    i_by = models.IntegerField()
    i_date = models.IntegerField()
    u_by = models.IntegerField()
    u_date = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'messages'


class NewPricingModel(models.Model):
    book_inv_id = models.IntegerField(primary_key=True)
    cola = models.FloatField(db_column='colA')  # Field name made lowercase.
    colb = models.FloatField(db_column='colB')  # Field name made lowercase.
    colc = models.FloatField(db_column='colC')  # Field name made lowercase.
    cold = models.FloatField(db_column='colD')  # Field name made lowercase.
    cole = models.FloatField(db_column='colE')  # Field name made lowercase.
    colf = models.FloatField(db_column='colF')  # Field name made lowercase.
    weight = models.FloatField()
    mrp = models.FloatField()
    new_price = models.FloatField()
    old_price = models.FloatField()
    shipping = models.FloatField()
    handling = models.FloatField()

    class Meta:
        managed = False
        db_table = 'new_pricing_model'


class OrderAddress(models.Model):
    order_id = models.IntegerField()
    rec_name = models.CharField(max_length=255)
    email = models.CharField(max_length=50, blank=True, null=True)
    pincode = models.IntegerField()
    address = models.TextField()
    landmark = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    phone = models.CharField(max_length=50)
    courier_name = models.CharField(max_length=255, blank=True, null=True)
    awb = models.CharField(max_length=255, blank=True, null=True)
    i_date = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'order_address'


class OrderBooks(models.Model):
    order_book_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField()
    book_id = models.IntegerField()
    book_inv_id = models.CharField(max_length=225)
    qty = models.IntegerField()
    racks = models.CharField(max_length=225)
    handling_charge = models.CharField(max_length=255)
    is_thanks_mail_sent = models.CharField(max_length=1)
    is_book_found = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'order_books'


class OrderNotes(models.Model):
    order_note_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField()
    note = models.TextField()
    note_type = models.CharField(max_length=1)
    is_read = models.CharField(max_length=10)
    i_by = models.IntegerField()
    i_date = models.IntegerField()
    u_by = models.IntegerField()
    u_date = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'order_notes'


class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_no = models.CharField(max_length=255, blank=True, null=True)
    user_id = models.IntegerField()
    amount = models.FloatField()
    no_of_book = models.IntegerField()
    status = models.IntegerField()
    payusing = models.CharField(max_length=225)
    checkouttype = models.CharField(max_length=1)
    biiling_add_id = models.IntegerField()
    shipping_add_id = models.IntegerField()
    i_by = models.IntegerField()
    i_date = models.IntegerField()
    u_by = models.IntegerField()
    u_date = models.IntegerField()
    is_thanks_mail_sent = models.CharField(max_length=1)
    is_notification_sent = models.CharField(max_length=1)
    fast_delivery = models.IntegerField()
    handling_charge = models.FloatField()
    cod_charge = models.CharField(max_length=255, blank=True, null=True)
    user_rating = models.IntegerField(blank=True, null=True)
    coupon_id = models.IntegerField(blank=True, null=True)
    coupon_amount = models.IntegerField()
    cod_offer_interested = models.IntegerField()
    actual_date_upload = models.DateField(blank=True, null=True)
    wallet_used = models.CharField(max_length=1000)
    courier_name = models.TextField(blank=True, null=True)
    weight = models.CharField(max_length=255, blank=True, null=True)
    expected_price = models.CharField(max_length=255, blank=True, null=True)
    shipment_tracking_no = models.CharField(max_length=100, blank=True, null=True)
    payment_url = models.CharField(max_length=255, blank=True, null=True)
    payment_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orders'


class Payments(models.Model):
    payment_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField()
    transacion_id = models.CharField(max_length=225)
    payment_details = models.TextField(blank=True, null=True)
    payvia = models.TextField()

    class Meta:
        managed = False
        db_table = 'payments'


class PinMap(models.Model):
    pincode = models.DecimalField(max_digits=38, decimal_places=0)
    taluk = models.CharField(max_length=50, blank=True, null=True)
    districtname = models.CharField(max_length=50)
    statename = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'pin_map'


class Pincodes(models.Model):
    pincode = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pincodes'


class Preferences(models.Model):
    preferences_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    recommended_books_notification = models.CharField(max_length=1)
    out_of_stocks_books_notification = models.CharField(max_length=1)
    books_status_changes_notification = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'preferences'


class Privileges(models.Model):
    privilege_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    is_allow_user_mgnt = models.IntegerField()
    is_allow_user_mgnt_write = models.IntegerField()
    is_allow_book_mgnt = models.IntegerField()
    is_allow_book_mgnt_write = models.IntegerField()
    is_allow_customer_data_mgnt = models.IntegerField()
    is_allow_customer_data_mgnt_write = models.IntegerField()
    is_allow_order_mgnt = models.IntegerField()
    is_allow_order_mgnt_write = models.IntegerField()
    is_allow_donation_req_mgnt = models.IntegerField()
    is_allow_donation_req_mgnt_write = models.IntegerField()
    is_allow_donor_mgnt = models.IntegerField()
    is_allow_donor_mgnt_write = models.IntegerField()
    is_allow_volunteer_req_verification_mgnt = models.IntegerField()
    is_allow_volunteer_req_verification_mgnt_write = models.IntegerField()
    is_allow_volunteer_mgnt = models.IntegerField()
    is_allow_volunteer_mgnt_write = models.IntegerField()
    is_allow_message_mgnt = models.IntegerField()
    is_allow_message_mgnt_write = models.IntegerField()
    is_allow_report_manipulation = models.IntegerField()
    is_allow_report_manipulation_write = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'privileges'


class Roles(models.Model):
    role_id = models.AutoField(primary_key=True)
    for_type = models.CharField(max_length=1)
    role = models.CharField(max_length=100)
    is_active = models.CharField(max_length=1)
    is_deleted = models.CharField(max_length=1)
    i_by = models.IntegerField()
    i_date = models.IntegerField()
    u_by = models.IntegerField()
    u_date = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'roles'


class Settings(models.Model):
    setting_id = models.AutoField(primary_key=True)
    var_name = models.CharField(max_length=255)
    var_value = models.TextField()

    class Meta:
        managed = False
        db_table = 'settings'


class Shipping(models.Model):
    shipping_id = models.AutoField(primary_key=True)
    sp_class = models.CharField(max_length=225)
    sp_amount = models.FloatField()
    is_active = models.CharField(max_length=1)
    is_deleted = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'shipping'


class States(models.Model):
    state_id = models.AutoField(primary_key=True)
    country_id = models.IntegerField()
    state_name = models.CharField(max_length=100)
    state_code = models.CharField(max_length=10, blank=True, null=True)
    is_active = models.CharField(max_length=1)
    is_deleted = models.CharField(max_length=1)
    i_by = models.IntegerField()
    i_date = models.IntegerField()
    u_by = models.IntegerField()
    u_date = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'states'


class UserRate(models.Model):
    user_rate_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=225, blank=True, null=True)
    email = models.CharField(max_length=225, blank=True, null=True)
    rate_type = models.IntegerField()
    rate = models.IntegerField()
    book_id = models.IntegerField(blank=True, null=True)
    order_id = models.IntegerField(blank=True, null=True)
    i_date = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_rate'


class UserReview(models.Model):
    user_review_id = models.AutoField(primary_key=True)
    user_rate_id = models.IntegerField()
    user_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=225)
    review_type = models.IntegerField()
    published = models.CharField(max_length=1)
    is_deleted = models.CharField(max_length=1)
    review = models.TextField()
    book_id = models.IntegerField(blank=True, null=True)
    order_id = models.IntegerField(blank=True, null=True)
    i_date = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_review'


class Useraddresses(models.Model):
    address_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    title = models.CharField(max_length=225, blank=True, null=True)
    rec_name = models.CharField(max_length=225, blank=True, null=True)
    pincode = models.IntegerField()
    address = models.TextField()
    landmark = models.CharField(max_length=225)
    country_id = models.IntegerField()
    state_id = models.IntegerField()
    city_id = models.IntegerField()
    phone_no = models.CharField(max_length=50, blank=True, null=True)
    address_type = models.IntegerField()
    is_primary = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'useraddresses'


class UseraddressesDuplicate(models.Model):
    address_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    title = models.CharField(max_length=225)
    rec_name = models.CharField(max_length=225, blank=True, null=True)
    pincode = models.IntegerField()
    address = models.TextField()
    landmark = models.CharField(max_length=225)
    country_id = models.IntegerField()
    state_id = models.IntegerField()
    city_id = models.IntegerField()
    phone_no = models.CharField(max_length=50)
    address_type = models.IntegerField()
    is_primary = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'useraddresses_duplicate'


class Userpreferences(models.Model):
    user_id = models.IntegerField()
    recommended_book = models.CharField(max_length=10)
    out_of_stock_book = models.CharField(max_length=10)
    book_status_change = models.CharField(max_length=10)
    recommended_for_you = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'userpreferences'


class Users(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=50)
    alternative_email = models.CharField(max_length=50, blank=True, null=True)
    password = models.CharField(max_length=255)
    user_role_id = models.IntegerField()
    avatar = models.CharField(max_length=100, blank=True, null=True)
    birth_date = models.CharField(max_length=25, blank=True, null=True)
    communication_address = models.TextField(blank=True, null=True)
    mobile = models.CharField(max_length=50, blank=True, null=True)
    contact_no = models.CharField(max_length=100, blank=True, null=True)
    profession = models.CharField(max_length=1000, blank=True, null=True)
    contribution = models.TextField(blank=True, null=True)
    profile_percentage = models.IntegerField(blank=True, null=True)
    is_volunteer = models.CharField(max_length=1)
    is_donor = models.CharField(max_length=1)
    is_customer = models.CharField(max_length=1)
    is_verified = models.CharField(max_length=1)
    is_deleted = models.CharField(max_length=1)
    is_active = models.CharField(max_length=1)
    i_date = models.IntegerField()
    i_by = models.IntegerField()
    u_date = models.IntegerField()
    u_by = models.IntegerField()
    registered_date = models.DateField(blank=True, null=True)
    wallet_amount = models.CharField(max_length=1000)

    class Meta:
        managed = False
        db_table = 'users'


class WalletTransactions(models.Model):
    wallet_id = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=1000)
    user_email = models.CharField(max_length=1000)
    transaction_id = models.CharField(max_length=1000, blank=True, null=True)
    deposit = models.CharField(max_length=1000)
    withdrawl = models.CharField(max_length=1000)
    payvia = models.CharField(max_length=1000)
    comment = models.CharField(max_length=1000)
    time = models.DateTimeField()
    added_by = models.CharField(max_length=1000)

    class Meta:
        managed = False
        db_table = 'wallet_transactions'


class Wishlists(models.Model):
    wl_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    book_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'wishlists'
