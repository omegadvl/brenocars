$("#id_Cep").focusout(function(){
	$.ajax({
		url: 'https://viacep.com.br/ws/'+ $(this).val() +'/json',
		dataType: 'json',
		success: function(resposta){
			$("#id_Endereco").val(resposta.logradouro);
			$("#id_Cidade").val(resposta.localidade);
			$("#id_Bairro").val(resposta.bairro);
			$("#id_Estado").val(resposta.localidade);
			$("#id_UF").val(resposta.uf);
		}
    });
});