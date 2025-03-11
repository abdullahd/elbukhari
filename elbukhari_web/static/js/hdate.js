var _____WB$wombat$assign$function_____ = function(name) {return (self._wb_wombat && self._wb_wombat.local_init && self._wb_wombat.local_init(name)) || self[name]; };
if (!self.__WB_pmw) { self.__WB_pmw = function(obj) { this.__WB_source = obj; return this; } }
{
  let window = _____WB$wombat$assign$function_____("window");
  let self = _____WB$wombat$assign$function_____("self");
  let document = _____WB$wombat$assign$function_____("document");
  let location = _____WB$wombat$assign$function_____("location");
  let top = _____WB$wombat$assign$function_____("top");
  let parent = _____WB$wombat$assign$function_____("parent");
  let frames = _____WB$wombat$assign$function_____("frames");
  let opener = _____WB$wombat$assign$function_____("opener");

var fixd;
function isGregLeapYear(year)
{
return year%4 == 0 && year%100 != 0 || year%400 == 0;
}
function gregToFixed(year, month, day)
{
var a = Math.floor((year - 1) / 4);
var b = Math.floor((year - 1) / 100);
var c = Math.floor((year - 1) / 400);
var d = Math.floor((367 * month - 362) / 12);
if (month <= 2)
e = 0;
else if (month > 2 && isGregLeapYear(year))
e = -1;
else
e = -2;
return 1 - 1 + 365 * (year - 1) + a - b + c + d + e + day;
}
function Hijri(year, month, day)
{
this.year = year;
this.month = month;
this.day = day;
this.toFixed = hijriToFixed;
this.toString = hijriToString;
}
function hijriToFixed()
{
return this.day + Math.ceil(29.5 * (this.month - 1)) + (this.year - 1) * 354 +
Math.floor((3 + 11 * this.year) / 30) + 227015 - 1;
}
function hijriToString()
{
var months = new Array("محرم","صفر","ربيع أول","ربيع ثانى","جمادى أول","جمادى ثانى","رجب","شعبان","رمضان","شوال","ذو القعدة","ذو الحجة");
return this.day + " " + months[this.month - 1]+ " " + this.year;
}
function fixedToHijri(f)
{
var i=new Hijri(1100, 1, 1);
i.year = Math.floor((30 * (f - 227015) + 10646) / 10631);
var i2=new Hijri(i.year, 1, 1);
var m = Math.ceil((f - 29 - i2.toFixed()) / 29.5) + 1;
i.month = Math.min(m, 12);
i2.year = i.year;
i2.month = i.month;
i2.day = 1;
i.day = f - i2.toFixed() + 1;
return i;
}
var tod=new Date();
var weekday=new Array("الأحد","الإثنين","الثلاثاء","الأربعاء","الخميس","الجمعة","السبت");
var monthname=new Array("يناير","فبراير","مارس","إبريل","مايو","يونيو","يوليو","أغسطس","سبتمبر","أكتوبر","نوفمبر","ديسمبر");
var y = tod.getFullYear();
var m = tod.getMonth();
var d = tod.getDate();
var dow = tod.getDay();
document.write(weekday[dow] + " " + d + " " + monthname[m] + " " + y);
m++;
fixd=gregToFixed(y, m, d);
var h=new Hijri(1421, 11, 28);
h = fixedToHijri(fixd);
document.write(" ميلادى - " + h.toString() + " هجرى &nbsp;&nbsp;");

}
/*
     FILE ARCHIVED ON 11:42:03 Jul 07, 2022 AND RETRIEVED FROM THE
     INTERNET ARCHIVE ON 10:20:01 Mar 11, 2025.
     JAVASCRIPT APPENDED BY WAYBACK MACHINE, COPYRIGHT INTERNET ARCHIVE.

     ALL OTHER CONTENT MAY ALSO BE PROTECTED BY COPYRIGHT (17 U.S.C.
     SECTION 108(a)(3)).
*/
/*
playback timings (ms):
  captures_list: 0.535
  exclusion.robots: 0.019
  exclusion.robots.policy: 0.008
  esindex: 0.012
  cdx.remote: 5.602
  LoadShardBlock: 307.634 (3)
  PetaboxLoader3.datanode: 212.865 (4)
  PetaboxLoader3.resolve: 203.741 (2)
  load_resource: 129.355
*/