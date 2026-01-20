/**
 * LC Script
  */

function setSelectedIndex(element_id, valsearch) 
{
	// set the drop down list selected index of element 'element_id' by the value 'valsearch'
	// Loop through all the items in drop down list
	for (i = 0; i< element_id.options.length; i++)
	{ 
		if (element_id.options[i].value == valsearch)
		{
		// Item is found. Set its property and exit
		element_id.options[i].selected = true;
		break;
		}
	}
	return;
}

function show(element_id)
{
	// show the element 'element_id'
	document.getElementById(element_id).style.display = 'block';
}

function hide(element_id)
{
	// hide the element 'element_id'
	document.getElementById(element_id).style.display = 'none';
}

function showhide(element_id)
{
	// show/hide the element 'element_id'
	if(document.getElementById(element_id).style.display == 'block')
	{
		document.getElementById(element_id).style.display = 'none';
	}
	else
	{
		document.getElementById(element_id).style.display = 'block';
	}
}

function toggle(show_id, hide_id)
{
	// toggle the 2 elements 'show_id' and 'hide_id'
	document.getElementById(show_id).style.display == 'block';
	
	document.getElementById(hide_id).style.display = 'none';
}


