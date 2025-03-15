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

function version_compare(t,i){if(t===i)return 0;for(var a=t.split("."),n=i.split("."),l=Math.min(a.length,n.length),e=0;l>e;e++){if(parseInt(a[e])>parseInt(n[e]))return 1;if(parseInt(a[e])<parseInt(n[e]))return-1}return a.length>n.length?1:a.length<n.length?-1:0}jQuery(function(t){void 0===t.fn.on&&(t.fn.on=function(i,a,n,l){return"function"==typeof a?t(this.context).live(i,a):t(a).live(i,n,l),this}),t(document).on("click",".showerrors",function(){return t(".xdetailed-errors").toggle(),!1}),t(document).on("click",".shownotices",function(){return t(".xdetailed-updated").toggle(),!1}),t("form.widget_wysija").on("focus","input[placeholder]",function(){t(this).val()===t(this).attr("placeholder")&&t(this).val("")}),t("form.widget_wysija").on("blur","input[placeholder]",function(){""===t(this).val()&&t(this).val(t(this).attr("placeholder"))}),t("form.widget_wysija").on("focus","input.defaultlabels",function(){t(this).val()===t(this).attr("title")&&t(this).val("")}),t("form.widget_wysija").on("blur","input.defaultlabels",function(){""===t(this).val()&&t(this).val(t(this).attr("title"))}),t(document).on("submit","form.widget_wysija",function(i){if(i.preventDefault(),void 0!==wysijaAJAX.noajax)return t(this).validationEngine("validate");if(t(this).validationEngine("validate")===!0){var a=t(this).find('input[name="action"]').val(),n=t(this).find('input[name="controller"]').val(),l=t(this).attr("id"),e=t(this).serializeArray();wysijaAJAX.task=a,wysijaAJAX.controller=n,wysijaAJAX.formid=l,t.each(e,function(t,i){wysijaAJAX["data["+t+"][name]"]=i.name,wysijaAJAX["data["+t+"][value]"]=i.value}),t("#msg-"+l).html('<div class="allmsgs"><blink>'+wysijaAJAX.loadingTrans+"</blink></div>"),t("#"+l).fadeOut(),t.ajax({type:"post",url:wysijaAJAX.ajaxurl,data:wysijaAJAX,success:function(i){t("#msg-"+l).html('<div class="allmsgs"></div>'),i.result||t("#"+l).fadeIn(),t.each(i.msgs,function(i,a){t("#msg-"+l+" .allmsgs ."+i+" ul").length||t("#msg-"+l+" .allmsgs").append('<div class="'+i+'"><ul></ul></div>'),t.each(a,function(a,n){t("#msg-"+l+" .allmsgs ."+i+" ul").append("<li>"+n+"</li>")})})},error:function(i,a,n){t("#msg-"+l).html('<div class="allmsgs"></div>'),t("#msg-"+l+" .allmsgs").html('<div class="error"><ul><li>Oops! There is a problem with this form:</li><li>textStatus:'+a+"</li><li>errorThrown:"+n+"</li><li>responseText:"+i.responseText+"</li></ul></div>")},dataType:"jsonp"})}return!1}),t(function(){var i="centerRight";wysijaAJAX.is_rtl&&(i="centerLeft"),t("form.widget_wysija").validationEngine("attach",{promptPosition:i,scroll:!1}),t("form.widget_wysija").bind("jqv.form.validating",function(){t(this).find("input[placeholder]").each(function(){t(this).val()===t(this).attr("placeholder")&&t(this).val("")})}),t("form.widget_wysija").find("input[placeholder]").each(function(){""===t(this).val()&&t(this).val(t(this).attr("placeholder"))}),t("form.widget_wysija").bind("jqv.form.validating",function(){t(this).find("input.defaultlabels").each(function(){t(this).val()===t(this).attr("title")&&t(this).val("")})}),t("form.widget_wysija").find("input.defaultlabels").each(function(){""===t(this).val()&&t(this).val(t(this).attr("title"))})})});

}
/*
     FILE ARCHIVED ON 11:42:03 Jul 07, 2022 AND RETRIEVED FROM THE
     INTERNET ARCHIVE ON 10:20:03 Mar 11, 2025.
     JAVASCRIPT APPENDED BY WAYBACK MACHINE, COPYRIGHT INTERNET ARCHIVE.

     ALL OTHER CONTENT MAY ALSO BE PROTECTED BY COPYRIGHT (17 U.S.C.
     SECTION 108(a)(3)).
*/
/*
playback timings (ms):
  captures_list: 10.815
  exclusion.robots: 0.019
  exclusion.robots.policy: 0.009
  esindex: 0.016
  cdx.remote: 24.589
  LoadShardBlock: 71.377 (3)
  PetaboxLoader3.datanode: 428.911 (6)
  load_resource: 1098.288 (2)
  PetaboxLoader3.resolve: 710.602 (2)
  loaddict: 45.485
*/