function h2p(){
	var pdf= new jsPDF('p', 'pt', 'letter');
			alert("dfcgvhbn");
	source= $('#QR_img')[0];
	specialElementHandlers = {
		'#bypassme': function(element, renderer){
						return true}
					}
	margins = {
		top: 50,
		left: 60,
		width: 545
	  };			
	alert("kvbkjdv2");
	
	pdf.fromHTML(source
	,margins.left
	,margins.top
	,{
		'width': margins.width
		,'elementHandlers':specialElementHandlers
	},
	function (dispose){
			pdf.save('save.pdf');
			}
			)
}