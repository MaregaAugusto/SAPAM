$(function(){
var provinciaOptions;
var ciudadOptions;
var filtro;
	$.getJSON('provincias.json',function(result){
		$.each(result, function(i,provincias) {
			provinciaOptions+="<option value='"
			+provincias.id+
			"'>"
			+provincias.nombre+
			"</option>";
			});
	});
	$("#provincia").change(function(){
		ciudadOptions="";
		filtro = ($(this).val()).toString();
		console.log(filtro)
			$.getJSON('municipios.json',function(result){
			$.each(result, function(j,ciudad) {
				if(filtro==ciudad.provincia.id){
					ciudadOptions+="<option value='"
					+ciudad.id+
					"'>"
					+ciudad.nombre+
					"</option>";
					}
				});
		});
	});
});
