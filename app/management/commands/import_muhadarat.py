from django.core.management.base import BaseCommand
from wagtail.documents.models import Document
from wagtail.blocks import StreamBlockValidationError
from wagtail.fields import StreamField
from wagtail import blocks
from wagtailmedia.blocks import AudioChooserBlock
from wagtailmedia.models import Media
from app.models import *

class Command(BaseCommand):
    help = 'Insert audios'

    def add_audios(self, audios, ModelName):
        for title, filename in audios:
            try:
                document = Media.objects.get(file__endswith=filename)
                media_content = StreamField([
                    ('audio', blocks.StructBlock([
                        ('audio_file', AudioChooserBlock()),
                    ]))
                ])
                media_content_value = [{
                    'type': 'audio',
                    'value': {'audio_file': document.id}
                }]
                
                audio = ModelName(title=title, media_content=media_content_value)
                audio.save()
                self.stdout.write(self.style.SUCCESS(f"Inserted '{title}' with file '{filename}'"))
            
            except Document.DoesNotExist:
                self.stdout.write(self.style.ERROR(f"Document '{filename}' not found in Wagtail Documents"))
            except StreamBlockValidationError as e:
                self.stdout.write(self.style.ERROR(f"StreamField validation error for '{title}': {e}"))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"Error inserting '{title}': {e}"))

    def handle(self, *args, **options):
        lectures = [('غربة-أهل-السنة', 'ghurbah-ahlus-sunnah.mp3'),
                    ('التحذير من التسرع في التكفير', 'at_tahdheer_min_at_tassaru_fit_takfeer.mp3'),
                    ('التحذير من آفة العجب', 'at_tahdheer_min_afat_il_ujb.mp3'),
                    ('المحافظة على الوقت', 'al_muhafadha_alal_waqt.mp3'),
                    ('الحث على الرفق', 'al_hath_alar_rifq.mp3'),
                    ('وصايا في طلب العلم (الجزء الأول ). المجلس الثالث من المجالس العلمية الرمضانية بجامع الرضوان عام 1438هـ', 'al_majalis_al_ilmiya_ar_ramadaniyah_1438_sh_bukhary_004.mp3'),
                    ('وصايا في طلب العلم (الجزء الثاني). المجلس الرابع من المجالس العلمية الرمضانية بجامع الرضوان عام 1438هـ', 'al_majalis_al_ilmiya_ar_ramadaniyah_1438_sh_bukhary_004-1.mp3'),
                    ('نصيحة موجهة لبعض الإخوة التائبين من مذهب الخوارج', 'nasiha_lit_taibeen_min_madhab_il_khawarij.mp3'),
                    ('التأييد لقرار الدولة السديد في قتل الفئة الإرهابية وتطبيق شرع الله المجيد', 'at_tayeed_li_qarar_id_dawlati_is_sadid.mp3'),
                    ('مسالك أهل الانحراف الفكري في تقرير أباطيلهم &#8211; الجزء الثاني', 'masalik_ahlul_inhiraf_il_fikry_part2.mp3'),
                    ('مسالك أهل الانحراف الفكري في تقرير أباطيلهم &#8211; الجزء الأول', 'masalik_ahlul_inhiraf_il_fikry_part1.mp3'),
                    ('أهمية تحلي طلاب العلم بالأخلاق النبوية وأثره في دفع الخلافات', 'ahamiyyat_thally_tulab_il_ilm_bil_akhlaq_0129.mp3'),
                    ('وصايا مهمة للمتخرجين من الجامعة الإسلامية', 'wsaya_mtkhrjen_algameah_aleslameah_0128.mp3'),
                    ('كلمة توجيهية لطلاب العلم الجزائريين', 'klmah_twjyhyah_letlab_algzareen_0127.mp3'),
                    ('فضل التمسك بالسنة', 'fdel_altmsk_bel_alsunah_0126.mp3'),
                    ('شرح أثر ابن سيرين رحمه الله «إن هذا العلم دين&#8230;»', 'shreh_ather_abn_syryn_0125.mp3'),
                    ('توجيهات أثرية في الارتقاء بالدعوة السلفية', 'twjehat_athryah_alart8a_alslfyah_0124.mp3'),
                    ('تسليط الأضواء على خصال الأولياء', 'tslet_aladwa_ala_khesal_alawlya_0123.mp3'),
                    ('تحذير أهل الإيمان من اتباع خطوات الشيطان', 'tahther_etba3_khtwat_alshytan_0122.mp3'),
                    ('الثبات على السنة', 'althbat_ala_alsunah_0121.mp3'),
                    ('وقليل من عبادي الشكور', 'wa_qalil_min_ibadea_alshukoor_0120.mp3'),
                    ('وصية بالتقوى والعمل بالعلم', 'waseyah_bel_tagwa_wa_alamel_bel_eleim_0119.mp3'),
                    ('وصايا لطالب العلم الشرعي', 'wasaya_letalib_alelim_alsharee_0118.mp3'),
                    ('وجوب الاجتماع والائتلاف ونبذ الفرقة والاختلاف', 'wujob_alejtemaa_wa_nabeth_alegtelaf_0117.mp3'),
                    ('من ثمرات التمسك بالسنة', 'men_thamarat_altamasuk_bel_sunna_0116.mp3'),
                    ('من أصول أهل السنة التميز والتمايز في زمن الفتن', 'min_usol_ahel_alsuna_altamayuz_fe_alfetan_0115.mp3'),
                    ('لقاء مفتوح في الجهراء بالكويت', 'liqa_muftooh_bil_jahra_0114.mp3'),
                    ('لقاء مفتوح في الجهراء بالكويت 1430', 'liqa_muftooh_bil_jahra_1430_0113.mp3'),
                    ('عليكم بسنتي', 'alaykum_bisunnati_0112.mp3'),
                    ('فضل العلم &#8211; لقاء هاتفي مع الإخوان في هولندا', 'fadl_alelem_wa_legaa_maa_holandeen_0111.mp3'),
                    ('عباد الرحمن إياكم وسبل الشيطان', 'ebad_alrahman_eyakum_wa_sobel_alshaetan_0110.mp3'),
                    ('طلب العلم السني الصحيح طريق النجاة من الهلاك', 'talab_alelem_alsony_najat_min_allhalak_0109.mp3'),
                    ('صوم رمضان', 'sawm_ramadan_0108.mp3'),
                    ('شكر النعم ولزوم الحق', 'shukr_alniam_wa_luzoom_alhaqq_0107.mp3'),
                    ('رسالة إلى طالب العلم', 'risalah_ela_talib_alelilm_0106.mp3'),
                    ('حقوق الأبناء', 'huqooq_alabnaa_0105.mp3'),
                    ('حسن السؤال مفتاح العلم', 'husn_alsoal_meftahh_alelem_0104.mp3'),
                    ('حال السلف مع القرآن', 'hall_alsalaf_ma_alquran_0103.mp3'),
                    ('جلسة علمية مفتوحة في دورة مكة عام 1429', 'jalsah_maftooh_makkah_1429_0102.mp3'),
                    ('تقوى الله عز وجل', 'taqwa_allah_0101.mp3'),
                    ('تعظيم سنة الرسول صلى الله عليه وسلم', 'tadhim_sunnah_alrasol_0100.mp3'),
                    ('تذكير الشيخ الفاضل باستمرار الصراع بين الحق والباطل', 'tadhkeer_alshaykh_be_estmrar_alserahe_099.mp3'),
                    ('تأملات في قول الله تعالى {يَا أَهْلَ الْكِتَابِ قَدْ جَاءكُمْ رَسُولنا} الآية', 'teamulat_fe_qawl_illahi_ya_ahl_alkitab_98.mp3'),
                    ('الضروريات الخمس وأهمية ارتباط الأمة بالعلماء', 'aldarooriyat_alkhames_097.mp3'),
                    ('الذين أوتوا العلم والإيمان', 'allatheen_utoo_alilma_wa_aleman_096.mp3'),
                    ('الخوارج', 'al_khawarej_095.mp3'),
                    ('التمييز والتمايز', 'altamayuz_wa_altamiyuz_094.mp3'),
                    ('التحذير من ضلالات التونسي بشير', 'tahdhir_min_bashir_093.mp3'),
                    ('الاستعداد لشهر رمضان', 'al_istidad_li_shahri_ramadan_092.mp3'),
                    ('الاحتجاج بالمتقدمين من مسائل الجاهلية', 'alehtejaj_bel_mutaqaddimeen_jahilia_091.mp3'),
                    ('الأسئلة الجزائرية عن القضايا المنهجية', 'alasila_alhjazairiyah_an_alqdaiya_almanhajeah_090.mp3'),
                    ('الأجوبة البخارية على الأسئلة الإماراتية والهولندية', 'ajoba_al_bukhariah_emirateah_wa_holandeah_089.mp3'),
                    ('نصيحة المحب في إرشاد طلاب المغرب', 'naseehat_ul_mihibb_fi_ershad_magreb_088.mp3'),
                    ('أوجه عمارة المساجد', 'aojah_emarat_almasajed_087.mp3'),
                    ('أهمية طلب العلم والعمل به', 'ahamiyatu_talab_al_ilm_wal_aml_bihi_086.mp3'),
                    ('أقسام الناس في معرفة الحق والباطل', 'aqsam_un_nas_fi_marfatil_haqq_wal_batil_085.mp3'),
                    ('أسباب ضعف أهل الحق', 'asbab_daf_ahl_il_haqq_084.mp3'),
                    ('وقفات مع مناظرة ابن عباس رضي الله عنهما للخوارج', 'mah_wagafaat_monazerh_Ibn_Abbas_le_alkhwarej_083.mp3'),
                    ('وصايا للسلفيين بهولندا', 'wasasya_le_salafian_be_holanda_082.mp3'),
                    ('وصايا سنية لمن أراد النجاة', 'wasasya_suniyah_liman_arad_alnajah_081.mp3'),
                    ('وصايا تتعلق بالعلم و طلبه', 'wasasya_tatalaq_bil_ilm_wa_talabih_080.mp3'),
                    ('وجوب لزوم الحق في أوقات الفتن', 'wejoob_luzoom_ul_hagg_waget_alfetann_079.mp3'),
                    ('هجر العوائد وقطع العوائق', 'hajr_al_awaid_wa_qata_alawaiq_078.mp3'),
                    ('نصائح وتوجيهات لطلبة الجامعة الإسلامية الجدد', 'nasaaih_wa_tawjeehaat_ltalbah_aljamah_077.mp3'),
                    ('نصائح في منهجية طلب العلم', 'fi_manhajiat_talab_ul_ilm_076.mp3'),
                    ('نبذة عن الخوارج المارقين', 'nubdhatun_an_alkhawarij_075.mp3'),
                    ('مواصلة الطاعات بعد انقضاء شهر الخيرات', 'muwaslat_ut_tait_074.mp3'),
                    ('من ثمرات التمسك بالسنة &#8211; قباء', 'min_thamarat_it_tamassuki_bis_sunnah_quba_073.mp3'),
                    ('من أسباب انشراح الصدر', 'min_asbab_inshirah_alsadr_072.mp3'),
                    ('معاناة أهل الإسلام وخاصة أهل السنة', 'muanat_ahl_alislam_071.mp3'),
                    ('ماذا بعد الحج؟', 'madha_bad_ul_hajj_070.mp3'),
                    ('ما يتعلق بالدعوة', 'ma_yatalaq_bid_dawah_069.mp3'),
                    ('ما هي السلفية؟', 'ma_hiyas_salafiyah_068.mp3'),
                    ('لقاء مفتوح للإجابة على الأسئلة الواردة عبر موقع ميراث الأنبياء', 'liqa_maftoh_26-09-1432_067.mp3'),
                    ('كيف يصلح المرء حاله', 'kaeff_salah_alhall_066.mp3'),
                    ('كلمة في الحياء', 'kalimah_fee_alhaiyaa_065.mp3'),
                    ('كلمة فضيلة الشيخ عبدالله في مسجد القدس بمدينة صبراتة', 'kalemah_masjed_Alqkds_misurata_064.mp3'),
                    ('كلمة عن الحج', 'kalimah_an_alhajj_063.mp3'),
                    ('كلمة ختامية لدورة «السنة للمزني» بالإمارات وصايا لطالب العلم', 'kalimah_khitamiyah_li_dawrat_as_sunnah_lilmuzany_uae_062.mp3'),
                    ('كلمة توجيهية لمنتديات التصفية والتربية السلفية', 'kalimatah_tawjihiyah_montadaeat_altasfeah_061.mp3'),
                    ('كلمة تذكيرية عن الحج', 'kalimah_tadhkeeriyah_an_alhajj_060.mp3'),
                    ('كلمة بخصوص حصار إخواننا في دماج', 'kalimah_bi_khusos_hisar_dammaj_059.mp3'),
                    ('فضل العلم وشرف أهله', 'fadl_ul_ilm_wa_sharfu_ahlih_058.mp3'),
                    ('فضل الدعوة إلى الحق والثبات عليه', 'fadl_ud_dawati_ilal_haqq_057.mp3'),
                    ('فضل التمسك بالسنة في زمن الغربة', 'fadl_ut_tamassuk_bis_sunnah_fi_zaman_il_ghurbah_056.mp3'),
                    ('طلب العلم', 'talab_ul_ilm_055.mp3'),
                    ('طلب العلم أهميته وآفاته', 'talab_ul_ilm_ahamiyatuhu_wa_afatuhu_054.mp3'),
                    ('ضوابط في الرد على المخالف', 'dawabit_fir_raddi_alal_mukhalif_053.mp3'),
                    ('صفة الرقية الشرعية وأخطاء الرقاة', 'sefah_arruqiyah_052.mp3'),
                    ('صفات الحدادية', 'sefat_ul_hadidiya_051.mp3'),
                    ('صدق الإتباع', 'sidq_ul_ittiba_050.mp3'),
                    ('شكر الله على نعمه', 'shukrullahi_ala_niamih_049.mp3'),
                    ('من حقوق الإخوة في الله', 'min_huqooq_il_ukhuwwah_048.mp3'),
                    ('شرح حديث العِبَادَةُ في الهرج كهجرة إليَّ', 'sharh_hadith_al_hijratu_fil_harj_047.mp3'),
                    ('شرح حديث «وأن لا تنازع الأمر أهله» &#8211; الجزء الأول', 'hadith_la_tonazaa_alamar_ahlah_dars1_045.mp3'),
                    ('شرح حديث «وأن لا تنازع الأمر أهله» &#8211; الجزء الثاني', 'hadith_la_tonazaa_alamar_ahlah_dars2_046.mp3'),
                    ('سؤالات أبي محمد الغامبي للشيخ البخاري &#8211; المجموعة الأولى', 'sualat_ul_ghambi_dars1_043.mp3'),
                    ('سؤالات أبي محمد الغامبي للشيخ البخاري &#8211; المجموعة الثانية', 'sualat_ul_ghambi_dars2_044.mp3'),
                    ('حقوق النبي عليه الصلاة والسلام', 'huqooq_alnabi_042.mp3'),
                    ('حق الرسول صلى الله عليه وسلم', 'haqq_alrrasool_041.mp3'),
                    ('جملة من الوصايا', 'jumlatun_min_al_wasaya_040.mp3'),
                    ('جريمة القول على الله بغير علم', 'jarimat_ul_qawl_alallahi_bighayri_ilm_039.mp3'),
                    ('تعظيم السنة', 'tadheem_alsunnah_038.mp3'),
                    ('تحذير النبلاء من طرائق أهل البدع والأهواء', 'tahdheer_un_nubala_min_taraiqi_ahl_il_bidai_wal_ahwa_037.mp3'),
                    ('تأملات في كلام شيخ الإسلام ابن تيمية في الأسباب المعينة على الصبر على أذى الخلق', 'teamulatun_fi_kalam_ibni_taimiyah_fis_sabr_036.mp3'),
                    ('تأملات في قول الله تعالى {وكذلك جعلناكم أمة وسطا}', 'tamulat_fi_wa_kadhalika_jalnaakum_ummatan_wasatan_035.mp3'),
                    ('تأملات في حديث «إن من أشراط الساعة أن يقل العلم ويظهر الجهل»', 'tamulat_fi_hadith_ashrat_is_saah_034.mp3'),
                    ('أهمية حسن الخلق والآداب', 'ahamiyat_husn_il_khuluqi_wal_adab_033.mp3'),
                    ('أهمية الوقت لطالب العلم', 'ahamiyat_al-waqt_li_talib_al-eilm_032.mp3'),
                    ('أهمية الصدق وآثاره الحميدة', 'ahammiyat_us_sidq_wa_atharh_alhamidh_031.mp3'),
                    ('أهمية اتباع السنة وخطر البدعة', 'ahammiyat__etebah_assunna_wa__khater_bidaa_masjid_alFarouqMt_030.mp3'),
                    ('الوقت وأهميته في حياة طالب العلم', 'ahamiyat_al-waqt_li_talib_al-eilm_029.mp3'),
                    ('الوصايا الذهبية', 'wasaya_dhahabiyah_028.mp3'),
                    ('الهجر في ضوء الكتاب والسنة', 'alhajer_doue_ketab_wu_alsonh_027.mp3'),
                    ('النصائح السلفية للإخوة في مسجد الرحمة بولاية نيوجرسي الأمريكية', 'al_nasaaih_as_salafiyah_new-Jersey_rahma_mosque_026.mp3'),
                    ('المخرج من الفتن هو الاعتصام بالكتاب والسنة', 'muhadaratal_makhraj_min_al_fitan_25.mp3'),
                    ('الفتن أنواعها وأسبابها وموقف المسلم منها', 'al_fitan_anoeaha_aspabha_024.mp3'),
                    ('العلم الشرعي وأثره في تحقيق الأمن', 'al_ilm_ush_shari_wa_atharuh_tahqiq_il_amn_023.mp3'),
                    ('الطريقة المثلى لرد تقرير أهل الباطل', 'at_tariqah_al_muthla_22.mp3'),
                    ('الصدق في لزوم السنة', 'as_sidq_fi_luzom_is_sunnah_021.mp3'),
                    ('الحياء', 'al-haya_020.mp3'),
                    ('الحث على طلب العلم', 'al_hath_ala_talab_il_ilm_19.mp3'),
                    ('الحث على الصدق', 'al_hath_alas_sidq_018.mp3'),
                    ('التواصي بالحق والصبر', 'at_tawasi_bil_haqq_was_sabr_017.mp3'),
                    ('التقوى حقيقتها وأثر تحقيقها', 'takwa_hakikateh_016.mp3'),
                    ('التعليق على مواضع من الرسالة التبوكية للإمام ابن القيم', 'at_taleeq_ala_mawadi_min_at_tabookiyah_15.mp3'),
                    ('التذكير بمداومة التوبة والاستغفار ووجوب العمل بالعلم', 'at_tadhkeer_bi_mudawamat_ut_tawbah_14.mp3'),
                    ('التحصن بالعلم &#8211; الإستعداد لرمضان &#8211; الرحلة إلى الجزائر', 'at_tahassun_bil_ilm_013.mp3'),
                    ('الإعتصام بحبل الله المتين', 'al_itisam_bi_habl_illah_012.mp3'),
                    ('الإجتماع والإختلاف', 'ijtima_wakhtilaf_011.mp3'),
                    ('أسئلة منهجية وحديثية', 'asilah_manhajiyah_wa_hadeethiyah_010.mp3'),
                    ('إستغلال الإجازة الصيفية واغتنام وقت الفراغ', 'estighlal_alejazah_alsayfiyah_009.mp3'),
                    ('أسباب الانحراف عن المنهج السلفي', 'asbab_ul_inhiraf_an_is_almanhj_alsalify_008.mp3'),
                    ('أسباب الانحراف عن السنة', 'asbab_ul_inhiraf_an_is_sunnah_007.mp3'),
                    ('أساليب أهل الأهواء والشبهات لتفريق الشباب السلفي', 'asaleb_ahoa_tafraiq_006.mp3'),
                    ('أدب السؤال وكيفية تعامل المسلم مع إخوانه', 'adab_alsoal_wa_taaml_the_muslim_with_brothers_005.mp3'),
                    ('آداب ووصايا لطالب علم الحديث', 'Adab_wa_wsaa-_talib_alm_alhdath_004.mp3'),
                    ('آداب ووصايا في طلب العلم', 'adab_wa_wsaa_tallb_alem_003.mp3'),
                    ('آداب طلب الحديث والسنة', 'Adab_Talb_Alhadit_002.mp3'),
                    ('إتباع الهوى يضل عن سبيل الهدى', 'Atba_Alahoa_001.mp3'),
                    ]
        
        lectures_2 = [
            ('النصائح السلفية للإخوة في مسجد الرحمة بولاية نيوجرسي الأمريكية', 'al_nasaaih_as_salafiyah_new-Jersey_rahma_mosque_026.mp3'),

        ]
        self.add_audios(audios=lectures_2, ModelName=Mohadarah)
