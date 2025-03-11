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

var shareBar = shareBar || (function(){
    var _args = {};
    return {
        init : function(Args) {
            _args = Args;
        },
        show : function(){
            var _buttonWidth = [];
            var _buttonWidthSmall = [];
            var additionalClass = '';
            if(_args['rtl'] == true){
                additionalClass = additionalClass+' sharebar-rtl';
            }
            var buttonCount = 0;
            var whatsappText = _args['text'].replace(/%25URL%25/,_args['url']).replace(/(%25NL%25)/g,'%0A');
            var twitterText = _args['text'].replace(/%25URL%25/,'').replace(/%25NL%25/g,' ');
            var button_fb = '';
            var button_twitter = '';
            var button_wa = '';
            var button_google = '';
            if(_args['whatsapp'] == true){ 
                if((navigator.userAgent.match(/(iPhone)/g) || navigator.userAgent.match(/(Android)/g))){
                    button_wa = '<a href="WhatsApp://send?text='+whatsappText+'" class="sharebar-button sharebar-whatsapp"><div>'+_args['share_wa']+'</div></a>';
                    buttonCount = buttonCount+1;
                }
            }
            if(_args['google'] == true){ 
                button_google = '<a href="https://web.archive.org/web/20240405202500/https://plus.google.com/share?url='+_args['url']+'" target="_blank" class="sharebar-button sharebar-google"><div>'+_args['share_g']+'</div></a>';
                buttonCount = buttonCount+1;
            }
            if(_args['facebook'] == true){ 
                button_fb = '<a href="https://web.archive.org/web/20240405202500/https://www.facebook.com/sharer/sharer.php?u='+_args['url']+'" target="_blank" class="sharebar-button sharebar-facebook"><div>'+_args['share_fb']+'</div></a>';
                buttonCount = buttonCount+1;
            }
            if(_args['twitter'] == true){ 
                button_twitter = '<a href="https://web.archive.org/web/20240405202500/https://twitter.com/intent/tweet?url='+_args['url']+'&text='+twitterText+'" target="_blank" class="sharebar-button sharebar-twitter"><div>'+_args['share_tw']+'</div></a>';
                buttonCount = buttonCount+1;
            }
            if(_args['position'] != 'top' && _args['position'] != 'bottom'){_args['position'] = 'top';}
            jQuery('body').prepend('<div id="mbl-sharebar" class="sharebar-'+_args['position']+' mbl-'+buttonCount+'-buttons'+additionalClass+'">'+button_fb+button_twitter+button_wa+button_google+'</div>');
            checkFontSize();
            checkOrientation();
            if( ((navigator.userAgent.match(/(Android)/g) || navigator.userAgent.match(/(webOS)/g) || navigator.userAgent.match(/(iPad)/g) || navigator.userAgent.match(/(iPod)/g) || navigator.userAgent.match(/(BlackBerry)/g) || navigator.userAgent.match(/(Windows Phone)/g)) && _args['everywhere'] == true && buttonCount > 1) || (navigator.userAgent.match(/(iPhone)/g) || navigator.userAgent.match(/(Android)/g))){
                jQuery(window).bind("scroll", function() {
                    checkFontSize();
                    checkOrientation();
                    if(jQuery('#mbl-sharebar').is(':hidden') && jQuery(window).scrollTop() > 150){
                        jQuery('#mbl-sharebar').show();
                    }else if(jQuery(window).scrollTop() <= 150){
                        jQuery('#mbl-sharebar').hide();
                    }
                });
                jQuery(window).bind("resize", function(){
                    checkFontSize();
                    checkOrientation();
                });
                jQuery(window).bind('orientationchange', function() {
                    checkFontSize();
                    checkOrientation();
                });
                jQuery('#mbl-sharebar .sharebar-button').each(function(index){

                });
            }
                function checkFontSize(){
                    var fontSize = (Math.floor(jQuery(window).width()/2*700/10000));
                    if(fontSize > 25){
                        fontSize = 25;
                    }
                    jQuery('#mbl-sharebar .sharebar-button').css({'font-size':fontSize+'px'});
                }
                function checkOrientation(){
                    jQuery('#mbl-sharebar').hide().removeClass('sharebar-landscape');
                    jQuery('#mbl-sharebar').css({'margin-top':'0px','margin-bottom':'0px'});
                    jQuery('#mbl-sharebar.sharebar-top').css({'top':'0px'});
                    jQuery('#mbl-sharebar.sharebar-bottom').css({'bottom':'0px'});
                    if(window.orientation != 0){
                        jQuery('#mbl-sharebar').addClass('sharebar-landscape');
                        jQuery('#mbl-sharebar.sharebar-top').css({'margin-top':(jQuery('#mbl-sharebar.sharebar-top').height()/-2)+'px'});
                        jQuery('#mbl-sharebar.sharebar-bottom').css({'margin-bottom':(jQuery('#mbl-sharebar.sharebar-bottom').height()/-2)+'px'});
                    }
                    if(jQuery('#mbl-sharebar').is(':hidden') && jQuery(window).scrollTop() > 150){
                        if( ((navigator.userAgent.match(/(Android)/g) || navigator.userAgent.match(/(webOS)/g) || navigator.userAgent.match(/(iPad)/g) || navigator.userAgent.match(/(iPod)/g) || navigator.userAgent.match(/(BlackBerry)/g) || navigator.userAgent.match(/(Windows Phone)/g)) && _args['everywhere'] == true && buttonCount > 1) || (navigator.userAgent.match(/(iPhone)/g) || navigator.userAgent.match(/(Android)/g))){
                            jQuery('#mbl-sharebar').show();
                        }
                    }
                }
        }
    };
}());



}
/*
     FILE ARCHIVED ON 20:25:00 Apr 05, 2024 AND RETRIEVED FROM THE
     INTERNET ARCHIVE ON 10:20:00 Mar 11, 2025.
     JAVASCRIPT APPENDED BY WAYBACK MACHINE, COPYRIGHT INTERNET ARCHIVE.

     ALL OTHER CONTENT MAY ALSO BE PROTECTED BY COPYRIGHT (17 U.S.C.
     SECTION 108(a)(3)).
*/
/*
playback timings (ms):
  captures_list: 0.503
  exclusion.robots: 0.017
  exclusion.robots.policy: 0.007
  esindex: 0.011
  cdx.remote: 4.939
  LoadShardBlock: 114.836 (3)
  PetaboxLoader3.datanode: 136.502 (5)
  PetaboxLoader3.resolve: 106.186 (2)
  load_resource: 146.68
  loaddict: 51.381
*/