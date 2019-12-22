window.onload=function()
{
	var a = [
	{
		"model":"models",
		"name":"Model S",
		"price": 123000,
		"year": 1230
	},
	{
		"model":"modelv",
		"name":"Model V",
		"price": 234000,
		"year": 2340
	},
	{
		"model":"modelk",
		"name":"Model K",
		"price": 345000,
		"year": 3450
	},
	];
	a.forEach
	(
		function(item,index)
		{
			listElement = document.createElement("th")
			listElement.id = item.model
			listElement.innerHTML = item.name
			document.getElementById("menu").appendChild(listElement)
		}
	)
	a.forEach(mouseoverHandler);
	function mouseoverHandler(item,index)
	{
		var b = document.getElementById(item.model);
		b.onmouseover = function()
		{
			document.getElementById("data-table").removeAttribute("hidden");
			document.getElementById("model").innerHTML=item.name;
			document.getElementById("price").innerHTML=item.price;
			document.getElementById("year").innerHTML=item.year;
		}
	}
};