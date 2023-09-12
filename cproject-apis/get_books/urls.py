from django.urls import path
from . import views

urlpatterns = [
	
	# for GET BOOKS & CATEGORY
	path('<int:pg>/',views.all_books),

	
	# COMPETITIVE EXAMS
	path('competitive-exams/<int:pg>/',views.competitive_exams),
	

	# COMPETITIVE EXAMS > CAT & its sub-categories	
	path('competitive-exams/cat/<int:pg>/', views.competitive_cat),


	# COMPETITIVE EXAMS > ENGINEERING & MEDICAL & its sub-categories
	path('competitive-exams/engineering/<int:pg>/', views.competitive_engg),
	path('competitive-exams/engineering/aieee/<int:pg>/',views.engg_aieee),
	path('competitive-exams/engineering/engineering-post-graduate/<int:pg>/', views.engg_postgrad),
	path('competitive-exams/engineering/iit/<int:pg>/', views.engg_iit),
	path('competitive-exams/engineering/medical/<int:pg>/', views.engg_medical),
	path('competitive-exams/engineering/others/<int:pg>/', views.engg_others),
	path('competitive-exams/engineering/state-level/<int:pg>/', views.engg_statelevel),


	# COMPETITIVE EXAMS > GENERAL KNOWLEDGE & LEARNING & its sub-categories
	path('competitive-exams/general-knowledge-learni/<int:pg>/', views.competitive_gk),
	path('competitive-exams/general-knowledge-learni/dic/<int:pg>/', views.gk_dict),
	path('competitive-exams/general-knowledge-learni/gk/<int:pg>/', views.gk_gk),	


	# COMPETITIVE EXAMS > GOVERNMENT JOBS & its sub-categories
	path('competitive-exams/government-jobs/<int:pg>/', views.competitive_govtjobs), 
	path('competitive-exams/government-jobs/banking/<int:pg>/', views.govtjobs_banking),
	path('competitive-exams/government-jobs/others/<int:pg>/', views.govtjobs_others),
	path('competitive-exams/government-jobs/railway/<int:pg>/', views.govtjobs_railway),
	path('competitive-exams/government-jobs/ssc/<int:pg>/', views.govtjobs_ssc),
	path('competitive-exams/government-jobs/teaching-related-exams/<int:pg>/', views.govtjobs_teachingexams),
	path('competitive-exams/government-jobs/upsc/<int:pg>/', views.govtjobs_upsc),	


	# COMPETITIVE EXAMS > INTERNATIONAL EXAMS & its sub-categories
	path('competitive-exams/international-exams/<int:pg>/', views.competitive_internationalexams),
	path('competitive-exams/international-exams/gmat/<int:pg>/', views.internationalexams_gmat),
	path('competitive-exams/international-exams/gre/<int:pg>/', views.internationalexams_gre),
	path('competitive-exams/international-exams/others/<int:pg>/', views.internationalexams_others),
	path('competitive-exams/international-exams/sat/<int:pg>/', views.internationalexams_sat),


	# COMPETITIVE EXAMS > SCHOOL LEVEL & its sub-categories
	path('competitive-exams/school-level/<int:pg>/', views.competitive_schoollevel),
	path('competitive-exams/school-level/navodaya-vidyalaya/<int:pg>/', views.schoollevel_navodaya),
	path('competitive-exams/school-level/ntse/<int:pg>/', views.schoollevel_ntse),
	path('competitive-exams/school-level/olympiads/<int:pg>/', views.schoollevel_olympiads),
	path('competitive-exams/school-level/others/<int:pg>/', views.schoollevel_others),
	path('competitive-exams/school-level/sainik-school/<int:pg>/', views.schoollevel_sainik),


	# FICTION NON-FICTION
	path('fiction-non-fiction/<int:pg>/',views.fiction_and_nonfiction),


	# FICTION NON-FICTION > FICTION & its sub-categories
	path('fiction-non-fiction/fiction/<int:pg>/', views.fiction_and_nonfiction__fiction),
	path('fiction-non-fiction/fiction/comics-graphic-novel/<int:pg>/', views.fiction_and_nonfiction__fiction_comics),
	path('fiction-non-fiction/fiction/drama/<int:pg>/', views.fiction_and_nonfiction__fiction_drama),
	path('fiction-non-fiction/fiction/horror-and-thriller/<int:pg>/', views.fiction_and_nonfiction__fiction_horrorthriller),
	path('fiction-non-fiction/fiction/humour/<int:pg>/', views.fiction_and_nonfiction__fiction_humour),
	path('fiction-non-fiction/fiction/literary/<int:pg>/', views.fiction_and_nonfiction__fiction_literary),
	path('fiction-non-fiction/fiction/mystery/<int:pg>/', views.fiction_and_nonfiction__fiction_mystery),
	path('fiction-non-fiction/fiction/romance/<int:pg>/', views.fiction_and_nonfiction__fiction_romance),
	path('fiction-non-fiction/fiction/science-fiction/<int:pg>/', views.fiction_and_nonfiction__fiction_sciencefiction),
	path('fiction-non-fiction/fiction/short-stories/<int:pg>/', views.fiction_and_nonfiction__fiction_shortstories),
	path('fiction-non-fiction/fiction/teens/<int:pg>/', views.fiction_and_nonfiction__fiction_teens),


	# FICTION NON-FICTION > FICTION & NON FICTION OTHERS & its sub-categories
	path('fiction-non-fiction/fiction-non-fiction-others/<int:pg>/', views.fiction_and_nonfiction__others),
	path('fiction-non-fiction/fiction-non-fiction-others/astrology/<int:pg>/', views.fiction_and_nonfiction__others_astrology),
	path('fiction-non-fiction/fiction-non-fiction-others/business-management/<int:pg>/', views.fiction_and_nonfiction__others_businessmgmt),
	path('fiction-non-fiction/fiction-non-fiction-others/health/<int:pg>/', views.fiction_and_nonfiction__others_health),
	path('fiction-non-fiction/fiction-non-fiction-others/history-and-politics/<int:pg>/', views.fiction_and_nonfiction__others_history),
	path('fiction-non-fiction/fiction-non-fiction-others/others/<int:pg>/', views.fiction_and_nonfiction__others_others),
	path('fiction-non-fiction/fiction-non-fiction-others/sports-games/<int:pg>/', views.fiction_and_nonfiction__others_sportgames),


	# FICTION NON-FICTION > MOTIVATION & SELF-HELP & its sub-categories
	path('fiction-non-fiction/motivation-self-help/<int:pg>/', views.fiction_and_nonfiction__motivationselfhelp),


	# FICTION NON-FICTION > NON FICTION & its sub-categories
	path('fiction-non-fiction/non-fiction/<int:pg>/', views.fiction_and_nonfiction__nonfiction),
	path('fiction-non-fiction/non-fiction/biographies/<int:pg>/', views.fiction_and_nonfiction__nonfiction_biographies),
	path('fiction-non-fiction/non-fiction/coffee-table/<int:pg>/', views.fiction_and_nonfiction__nonfiction_coffeetable),
	path('fiction-non-fiction/non-fiction/computer-and-internet/<int:pg>/', views.fiction_and_nonfiction__nonfiction_computer),
	path('fiction-non-fiction/non-fiction/cooking/<int:pg>/', views.fiction_and_nonfiction__nonfiction_cooking),
	path('fiction-non-fiction/non-fiction/entertainment/<int:pg>/', views.fiction_and_nonfiction__nonfiction_entertainment),
	path('fiction-non-fiction/non-fiction/househome/<int:pg>/', views.fiction_and_nonfiction__nonfiction_househome),
	path('fiction-non-fiction/non-fiction/pets/<int:pg>/', views.fiction_and_nonfiction__nonfiction_pets),
	path('fiction-non-fiction/non-fiction/photography/<int:pg>/', views.fiction_and_nonfiction__nonfiction_photography),
	path('fiction-non-fiction/non-fiction/sports/<int:pg>/', views.fiction_and_nonfiction__nonfiction_sports),
	path('fiction-non-fiction/non-fiction/travel/<int:pg>/', views.fiction_and_nonfiction__nonfiction_travel),


	# FICTION NON-FICTION > RELIGION & SPIRITUALITY & its sub-categories
	path('fiction-non-fiction/religion-spirituality/<int:pg>/', views.fiction_and_nonfiction__religion),
	path('fiction-non-fiction/religion-spirituality/holy-books/<int:pg>/', views.fiction_and_nonfiction__religion_holybooks),
	path('fiction-non-fiction/religion-spirituality/others/<int:pg>/', views.fiction_and_nonfiction__religion_others),
	path('fiction-non-fiction/religion-spirituality/philosophy/<int:pg>/', views.fiction_and_nonfiction__religion_philosophy),
	path('fiction-non-fiction/religion-spirituality/religions/<int:pg>/', views.fiction_and_nonfiction__religion_religions),
	path('fiction-non-fiction/religion-spirituality/spirituality/<int:pg>/', views.fiction_and_nonfiction__religion_spirituality),


	# NOTEBOOK
	path('note-book-/<int:pg>/',views.notebook),


	# SCHOOL & CHILDREN BOOKS
	path('school-children-books/<int:pg>/', views.schoolchildren),


	# SCHOOL & CHILDREN BOOKS > CHILDREN BOOKS & its sub-categories
	path('school-children-books/children-books/<int:pg>/', views.schoolchildren_children),
	path('school-children-books/children-books/action-and-adventure/<int:pg>/', views.schoolchildren_children_action),
	path('school-children-books/children-books/activity-books/<int:pg>/', views.schoolchildren_children_activitybooks),
	path('school-children-books/children-books/childrens-literature/<int:pg>/', views.schoolchildren_children_literature),
	path('school-children-books/children-books/comics-graphic-novels/<int:pg>/', views.schoolchildren_children_comics),
	path('school-children-books/children-books/disney-store/<int:pg>/', views.schoolchildren_children_disneystore),
	path('school-children-books/children-books/fun-humour/<int:pg>/', views.schoolchildren_children_funhumour),
	path('school-children-books/children-books/history-mythology-/<int:pg>/', views.schoolchildren_children_mythology),
	path('school-children-books/children-books/knowledge-and-learning/<int:pg>/', views.schoolchildren_children_knowledge),
	path('school-children-books/children-books/others/<int:pg>/', views.schoolchildren_children_others),
	path('school-children-books/children-books/picture-book/<int:pg>/', views.schoolchildren_children_picturebook),


	# SCHOOL & CHILDREN BOOKS > CLASSES & its sub-categories
	path('school-children-books/classes/<int:pg>/', views.schoolchildren_classes),
	path('school-children-books/classes/kg/<int:pg>/', views.schoolchildren_classes_kg),
	path('school-children-books/classes/class-1/<int:pg>/', views.schoolchildren_classes_class1),
	path('school-children-books/classes/class-2/<int:pg>/', views.schoolchildren_classes_class2),
	path('school-children-books/classes/class-3/<int:pg>/', views.schoolchildren_classes_class3),
	path('school-children-books/classes/class-4/<int:pg>/', views.schoolchildren_classes_class4),
	path('school-children-books/classes/class-5/<int:pg>/', views.schoolchildren_classes_class5),
	path('school-children-books/classes/class-6/<int:pg>/', views.schoolchildren_classes_class6),
	path('school-children-books/classes/class-7/<int:pg>/', views.schoolchildren_classes_class7),
	path('school-children-books/classes/class-8/<int:pg>/', views.schoolchildren_classes_class8),
	path('school-children-books/classes/class-9/<int:pg>/', views.schoolchildren_classes_class9),	
	path('school-children-books/classes/class-10/<int:pg>/', views.schoolchildren_classes_class10),
	path('school-children-books/classes/class-11/<int:pg>/', views.schoolchildren_classes_class11),
	path('school-children-books/classes/class-12/<int:pg>/', views.schoolchildren_classes_class12),


	# SCHOOL & CHILDREN BOOKS > NCERT & its sub-categories
	path('school-children-books/ncert/<int:pg>/', views.schoolchildren_ncert),
	path('school-children-books/ncert/class-6/<int:pg>/', views.schoolchildren_ncert_class6),	
	path('school-children-books/ncert/class-7/<int:pg>/', views.schoolchildren_ncert_class7),
	path('school-children-books/ncert/class-8/<int:pg>/', views.schoolchildren_ncert_class8),	
	path('school-children-books/ncert/class-9/<int:pg>/', views.schoolchildren_ncert_class9),	
	path('school-children-books/ncert/class-10/<int:pg>/', views.schoolchildren_ncert_class10),
	path('school-children-books/ncert/class-11/<int:pg>/', views.schoolchildren_ncert_class11),
	path('school-children-books/ncert/class-12/<int:pg>/', views.schoolchildren_ncert_class12),


	# SCHOOL & CHILDREN BOOKS > DICTIONARY LEVEL & its sub-categories
	path('school-children-books/dictionary-level-/<int:pg>/', views.schoolchildren_dictionary),
	path('school-children-books/dictionary-level-/english-to-english-/<int:pg>/', views.schoolchildren_dictionary_engtoeng),
	path('school-children-books/dictionary-level-/english-to-hindi-/<int:pg>/', views.schoolchildren_dictionary_engtohindi),
	path('school-children-books/dictionary-level-/foreign-language/<int:pg>/', views.schoolchildren_dictionary_foreign),
	path('school-children-books/dictionary-level-/hindi-to-english-/<int:pg>/', views.schoolchildren_dictionary_hintoeng),
	path('school-children-books/dictionary-level-/subject-wise-/<int:pg>/', views.schoolchildren_dictionary_subjectwise),


	# UNIVERSITY BOOKS
	path('university-books/<int:pg>/', views.university),

	
	# UNIVERSITY BOOKS > ENGINEERING & its sub-categories
	path('university-books/engineering/<int:pg>/', views.university_engg),
	path('university-books/engineering/aeronautical/<int:pg>/', views.university_engg_aeronautical),
	path('university-books/engineering/bio-technology/<int:pg>/', views.university_engg_biotechnology),
	path('university-books/engineering/chemical-/<int:pg>/', views.university_engg_chemical),
	path('university-books/engineering/civil-/<int:pg>/', views.university_engg_civil),
	path('university-books/engineering/computer-science/<int:pg>/', views.university_engg_computersci),
	path('university-books/engineering/electrical-/<int:pg>/', views.university_engg_electrical),
	path('university-books/engineering/electronics/<int:pg>/', views.university_engg_electronics),
	path('university-books/engineering/marine/<int:pg>/', views.university_engg_marine),
	path('university-books/engineering/mechanical/<int:pg>/', views.university_engg_mechanical),
	path('university-books/engineering/others/<int:pg>/', views.university_engg_others),


	# UNIVERSITY BOOKS > FINANCE & its sub-categories
	path('university-books/finance/<int:pg>/', views.university_finance),


	# UNIVERSITY BOOKS > MEDICAL & its sub-categories
	path('university-books/medical/<int:pg>/', views.university_medical),
	path('university-books/medical/ayurveda/<int:pg>/', views.university_medical_ayurveda),
	path('university-books/medical/dental/<int:pg>/', views.university_medical_dental),
	path('university-books/medical/mbbs/<int:pg>/', views.university_medical_mbbs),
	path('university-books/medical/others/<int:pg>/', views.university_medical_others),
	path('university-books/medical/pg/<int:pg>/', views.university_medical_pg),
	path('university-books/medical/pharmacy/<int:pg>/', views.university_medical_pharmacy),


	# UNIVERSITY BOOKS > OTHERS & its sub-categories
	path('university-books/others/<int:pg>/', views.university_others),
	path('university-books/others/bba/<int:pg>/', views.university_others_bba),
	path('university-books/others/bcom/<int:pg>/', views.university_others_bcom),
	path('university-books/others/law/<int:pg>/', views.university_others_law),
	path('university-books/others/mba/<int:pg>/', views.university_others_mba),
	path('university-books/others/mcom/<int:pg>/', views.university_others_mcom),
	path('university-books/others/others/<int:pg>/', views.university_others_others),
	path('university-books/others/phd/<int:pg>/', views.university_others_phd),
	path('university-books/others/probability-statistics/<int:pg>/', views.university_others_stats),


	# UNIVERSITY BOOKS > SCIENCE & ARTS & its sub-categories
	path('university-books/science-arts/<int:pg>/', views.university_sciencearts),
	path('university-books/science-arts/bca/<int:pg>/', views.university_sciencearts_bca),
	path('university-books/science-arts/bsc/<int:pg>/', views.university_sciencearts_bsc),
	path('university-books/science-arts/ma/<int:pg>/', views.university_sciencearts_ma),
	path('university-books/science-arts/mca/<int:pg>/', views.university_sciencearts_mca),
	path('university-books/science-arts/msc/<int:pg>/', views.university_sciencearts_msc),
	path('university-books/science-arts/ba/<int:pg>/', views.university_sciencearts_ba)

	]