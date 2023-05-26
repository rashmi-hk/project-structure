< dtml - if expr = "REQUEST.has_key('l')" >
< dtml - call
"REQUEST.set('langName', Get_Language_By_Id(l))" >
< dtml - elif expr = "REQUEST.has_key('langid')" >
< dtml - call
"REQUEST.set('langName', Get_Language_By_Id(langid))" >
< dtml - else >
< dtml - call
"REQUEST.set ('langName',ProductBrand.getBrandProperty(getBrandId(), 'defaultLanguage'))" >
< / dtml - if >

< dtml - if expr = "REQUEST.has_key('params')" >
< dtml - call
"REQUEST.set('accData', params)" >
< dtml - else >
< dtml - call
"REQUEST.set ('accData','')" >
< / dtml - if >

< !DOCTYPE
html >
< html >

< head >
< meta
name = "viewport"
content = "initial-scale=1,user-scalable=no,maximum-scale=1,width=device-width,height=device-height" >
< script
type = "text/javascript"
language = "javascript"
src = "javaScript/changeAccountPasswordMobile.js" > < / script >
< script
type = "text/javascript"
language = "javascript"
src = "javaScript/general.js?ver=<dtml-var expr="
getVersionNumber()
">" > < / script >
< script
type = "text/javascript"
language = "javascript"
src = "src/javaScript/XHConn.js?ver=<dtml-var expr="
getVersionNumber()
">" > < / script >

< link
rel = "shortcut icon"
href = "v2/ProductBrand/<dtml-var getBrandId>/icons/tab.ico" / >
< link
href = "ProductBrand/<dtml-var getBrandId>/styleSheets/changeAccountPassword.css?ver=<dtml-var expr="
getVersionNumber()
">"
rel = "stylesheet"
type = "text/css" / >
< dtml - if "Languages_Localizer.getLangDirection(langName) == 'rtl'" >
< link
href = "ProductBrand/<dtml-var getBrandId>/styleSheets/changeAccountPassword_rtl.css?ver=<dtml-var expr="
getVersionNumber()
">"
rel = "stylesheet"
type = "text/css" / >
< / dtml - if >
< / head >

< body
dir = "<dtml-var expr="
Languages_Localizer.getLangDirection(langName)
">" >

< table


class ="header" >

< tr >
< td > < center > < img
id = "header"
width = "380"
src = "ProductBrand/<dtml-var getBrandId>/imgs/iOS/header.png"
alt = "" > < / center > < / td >
< / tr >
< / table >

< center >
< input
type = "hidden"
value = "<dtml-var "
REQUEST['accData']
">"
id = "accData" / >
< dtml - if expr = "checkLinkIsValid()" >
< div
id = "changePasswordDiv"


class ="padding10" >

< br / > < br / >
< table
style = "width: 305px;" >
< tr >
< td >
< table
cellpadding = "0"
cellspacing = "0"
style = "width: 90%" >
< tr


class ="passwordTr" >

< td > < input
type = "password"


class ="passwordInput" id="password" name="password" placeholder="<dtml-var expr="Gui.Get_Page_Text_By_ID('change_account_password', 'newPassword', langName)">" > < / td >

< td
style = "width: 40px;" > < a
href = "#"
onclick = "showPassword(); return false;" > < img
id = "showPasswordIcon"
src = "ProductBrand/<dtml-var getBrandId>/icons/eye_icon_close.png"
width = "30" > < / a >
< input
type = "hidden"
id = "showPasswordIconSrc"
value = "ProductBrand/<dtml-var getBrandId>/icons/" / >
< / td >
< / tr >
< / table >
< / td >
< / tr >
< tr >
< td


class ="validator" >

< p
id = "emptyPassword"
style = "display: none;" > < dtml - var
expr = "Gui.Get_Page_Text_By_ID('change_account_password', 'emptyPassword', langName)" > < / p >
< p
id = "wrongLenght"
style = "display: none;" > < dtml - var
expr = "Gui.Get_Page_Text_By_ID('change_account_password', 'wrongLenght', langName)" > < / p >
< p
id = "invalidChars"
style = "display: none;" > < dtml - var
expr = "Gui.Get_Page_Text_By_ID('change_account_password', 'invalidChars', langName)" > < / p >
< p
id = "generalErrMsg"
style = "display: none;" > < dtml - var
expr = "Gui.Get_Page_Text_By_ID('change_account_password', 'generalErrMsg', langName)" > < / p >
< / td >
< / tr >
< tr >
< td


class ="passwordInstructions" >

< br / > < dtml - var
expr = "Gui.Get_Page_Text_By_ID('change_account_password', 'passwordInstructions', langName)" >
< / td >
< / tr >

< tr >
< td > < br / > < br / > < center > < a
id = "setPasswordBtn"


class ="btn" onclick="setAccountPassword();" > < dtml-var expr="Gui.Get_Page_Text_By_ID('change_account_password', 'changePassword', langName)" > < / a > < / center > < / td >

< / tr >
< / table >
< / from >
< / div >
< div
id = "successDiv"


class ="padding10" style="display: none;" >

< h3 > < dtml - var
expr = "Gui.Get_Page_Text_By_ID('change_account_password', 'success', langName)" > < / h3 >
< div


class ="passwordInstructions" >

< dtml - var
expr = "Gui.Get_Page_Text_By_ID('change_account_password', 'passwordChangedSuccessfully', langName)" > < br / > < br / >
< dtml - var
expr = "Gui.Get_Page_Text_By_ID('change_account_password', 'returnToSurfieToLogin', langName)" > < br / > < br / >
< / div >
< img
src = "ProductBrand/95/imgs/Mobile/logo.png"
alt = ""
width = "150" / >
< / div >

< dtml - else >
< div
id = "sendlinkExpired" >
< h3 > < dtml - var
expr = "Gui.Get_Page_Text_By_ID('change_account_password', 'hiThere', langName)" > < / h3 >
< dtml - var
expr = "Gui.Get_Page_Text_By_ID('change_account_password', 'linkExpired', langName)" >
< br / > < br / > < button


class ="btn" onclick="sendChangePasswordLink()" type="button" > < dtml-var expr="Gui.Get_Page_Text_By_ID('change_account_password', 'sendLinkAgain', langName)" > < / button >

< / div >

< div
id = "sendlinkAgainInfo"
style = "display: none;" >
< h3 > < dtml - var
expr = "Gui.Get_Page_Text_By_ID('change_account_password', 'changePassword', langName)" > < / h3 >
< dtml - var
expr = "Gui.Get_Page_Text_By_ID('change_account_password', 'weSentYouLink', langName)" > < br / >
< b
id = "sendEmailAddress" > < / b > < br / >
< dtml - var
expr = "Gui.Get_Page_Text_By_ID('change_account_password', 'pleaseOpenTheLinkToChangePassword', langName)" > < br / > < br / >
< / div >

< / dtml - if >

< / center >

< div
id = "disableDiv"


class ="fullscreen-container" >

< / div >

< dtml - comment >
< div
id = "generalPopup"


class ="popup" style="display: none;" >

< a
id = "closePopupBtn"


class ="closePopup" href="#" onclick="closePopup(); return false;" > < img src="/v2/ParentAppSettings/imgs/close_popup.png" / > < / a >

< div
id = "generalErr" >
< h3 > < dtml - var
expr = "Gui.Get_Page_Text_By_ID('forgot_password','Oops', langName)" > < / h3 >
< p
id = "emptyPassword" > < dtml - var
expr = "Gui.Get_Page_Text_By_ID('change_account_password', 'emptyPassword', langName)" > < / p >
< p
id = "wrongLenght" > < dtml - var
expr = "Gui.Get_Page_Text_By_ID('change_account_password', 'wrongLenght', langName)" > < / p >
< p
id = "invalidChars" > < dtml - var
expr = "Gui.Get_Page_Text_By_ID('change_account_password', 'invalidChars', langName)" > < / p >
< p
id = "generalErrMsg" < dtml - var
expr = "Gui.Get_Page_Text_By_ID('change_account_password', 'generalErrMsg', langName)" >> < / p >
< br / > < a
href = "#"


class ="popupLink" onclick="closePopup(); return false;" > < dtml-var expr="Gui.Get_Page_Text_By_ID('change_account_password', 'okThanks', langName)" > < / a >

< / div >
< / dtml - comment >

< / div >

< / body >
< / html >