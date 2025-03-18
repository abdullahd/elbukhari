from django.core.management.base import BaseCommand
from wagtail.documents.models import Document
from app.models import Khutbah  # Replace 'your_app' with your actual app name
from wagtail.blocks import StreamBlockValidationError
from wagtail.fields import StreamField
from wagtail import blocks
from wagtailmedia.blocks import AudioChooserBlock, VideoChooserBlock
from wagtailmedia.models import Media

class Command(BaseCommand):
    help = 'Inserts Khutbah titles and audio files into the Khutbah model'

    def handle(self, *args, **options):
        # List of khutbahs (title, filename)
        khutbahs = [
            ("خطر الوسوسة", "khutbah_1439-06-07.mp3"),
            ("مقتطفات من سيرة النبي ﷺ مع أهل بيته", "khutbah_1439-05-09.mp3"),
            ("معالم الاتباع", "maalim_ul_ittiba_25.mp3"),
            ("وجوب طاعة الرسول صلى الله عليه وسلم ومحبته", "wojob_taah_alrasol_24.mp3"),
            ("نعمة القرآن والتحذير من هجره", "nemah_alquran_0023.mp3"),
            ("فضل صلة الرحم وعقوبة قطيعتها", "fadel_selat_alrahom_22.mp3"),
            ("فضل أم المؤمنين عائشة رضي الله عنها والرد على الطاعنين فيها", "fadel_aisha_0021.mp3"),
            ("فضل العلم وشرف حملته", "fadel_alelem_0020.mp3"),
            ("فضل الصحابة -رضي الله عنهم- وحقوقهم على الأمة", "fadel_alsahabh_0019.mp3"),
            ("فضائل الأعمال في شهر رمضان", "fdiel_-alaamal_ramadan_0018.mp3"),
            ("عليكم بالطاعة والجماعة -المدينة", "aliykom_btaah_almadenh_0017.mp3"),
            ("عليكم بالطاعة والجماعة – الجزائر", "aliykom_btaah_algeria_0016.mp3"),
            ("ذم الرشوة", "zam_alrashoh_0015.mp3"),
            ("خطورة التهاون بالصلاة المفروضة", "Khtourh_althawon_alsalt_0014.mp3"),
            ("حكم سب النبي صلى الله عليه وسلم", "hokom_sapp_alnabe_0013.mp3"),
            ("حقوق ولاة الأمور المسلمين", "hokouk_Wolat_alomowr_0012.mp3"),
            ("حقوق الأولاد على الوالدين بعد ميلادهم", "hokouk_alwallad_baad_aloladh_0010.mp3"),
            ("حسن العشرة بين الزوجين", "hosan_-alecherh_alzojian_0009.mp3"),
            ("ثمرات سلامة القلب وعلاماتها", "tmarat_salamh_algulob_0008.mp3"),
            ("تحذير المسلمين من الخوارج المحدثين", "thazer_mena_khoarej_0007.mp3"),
            ("الصلاة أهميتها وفضلها وإقامتها", "alsalt_ahmeatha_0006.mp3"),
            ("الشائعات خطرها والموقف الصحيح منها", "achaiat_katrha_0005.mp3"),
            ("البكاء من خشية الله", "albca_men_kacheh_allah_0004.mp3"),
            ("الإيمان بحوض النبي صلى الله عليه وسلم", "aleman_bhod_alnabe_0003.mp3"),
            ("الأمن مفهومه وحاجة الناس إليه", "Alomn_mfhomh_wa_hajah_alnas_elieh_0002.mp3"),
            ("أسباب غلاء الأسعار وعلاجه", "Acepab-glae-Alasear_0001.mp3"),
        ]

        for title, filename in khutbahs:
            try:
                # Look up the document by filename
                document = Media.objects.get(file__endswith=filename)
                
                # Create the StreamField content with AudioBlock
                media_content = StreamField([
                    ('audio', blocks.StructBlock([
                        ('audio_file', AudioChooserBlock()),
                    ]))
                ])
                media_content_value = [
                    {
                        'type': 'audio',
                        'value': {
                            'audio_file': document.id,
                        }
                    }
                ]
                
                # Create and save the Khutbah instance
                khutbah = Khutbah(
                    title=title,
                    media_content=media_content_value
                )
                khutbah.save()
                
                self.stdout.write(self.style.SUCCESS(f"Inserted '{title}' with file '{filename}'"))
            
            except Document.DoesNotExist:
                self.stdout.write(self.style.ERROR(f"Document '{filename}' not found in Wagtail Documents"))
            except StreamBlockValidationError as e:
                self.stdout.write(self.style.ERROR(f"StreamField validation error for '{title}': {e}"))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"Error inserting '{title}': {e}"))
