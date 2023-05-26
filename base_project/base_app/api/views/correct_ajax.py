console.log("EVENT");
function
get_checkbox(event)
{
    console.log("getCheckbox", event.target.checked)
    if (event.target.checked)
{
    console.log("call API");
console.log("Inside event", event.target)

} else {
    console.log("checkbox is not checked");
}
}

function
testParentResponse(response)
{
    alert(response);
}

function
get_child_checkbox_details(event)
{
    console.log("childe log ====>", event.target.name);
strParams = "appId=" + event.target.value
path = "https://surfie-t.puresight.com/ParentAppSettings/IOsApplicationManagment/testAjax";
psAjaxRequest(path, strParams, 'testResponse', 'POST', "appTime.html");

}

function
testResponse(response)
{
    alert(response);
}


