window.onload = function()
{
  var details=
  {
    name:"SVK",
    aadhar: 1024102410241024,
    labtests: ["x-ray","blood test"]
  };
  var hospitals=
  {
    name: "APOLLO HOSPITAL",
    location: "BILASPUR"
  };

  var a = document.getElementById("hospital");
  a.innerHTML = hospitals["name"] + " : " + hospitals["location"];
  
  var b = document.getElementById("patient");
  b.addEventListener("mouseover",function (e)
  {
    e.target.style.color = "orange";
    var c = document.getElementById("details");
    c.innerHTML = details["name"]+":"+ details["aadhar"];
    var test = "";
    details["labtests"].forEach(function(a)
    {
      test += a + "   ";
    });
    var d = document.getElementById("tests");
    d.innerHTML = test;
  });
};

