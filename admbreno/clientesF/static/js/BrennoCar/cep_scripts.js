$("#id_cep").focusout(function(){
	$.ajax({
		url: 'https://viacep.com.br/ws/'+ $(this).val() +'/json',
		dataType: 'json',
		success: function(resposta){
			$("#id_endereco").val(resposta.logradouro);
			$("#id_cidade").val(resposta.localidade);
			//$("#id_bairro").val(resposta.bairro);
			$("#id_estado").val(resposta.localidade);
			$("#id_uf").val(resposta.uf);
		}
    });
});