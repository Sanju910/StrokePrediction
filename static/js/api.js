$(document).ready(function(e) {

    $('#makePred').click(function() {

        $('#hfProb').empty();
        // $('#hfPred').empty();

        var gender=$('#sex').val();
        var age=$('#age').val();
        var hypertension=$('#hypertension').val();
        var heart_disease = $('#heart_disease').val();
        var ever_married = $('#Marriage').val();
        var work_type = $('#WorkType').val();
        var Residence_type = $('#Residence').val();
        var avg_glucose_level = $('#glucose').val();
        var bmi = $('#bmi').val();
        var smoking_status = $('#smoking').val();

        var inputData = {"gender":gender,"age":age,"hypertension":hypertension,"heart_disease":heart_disease,"ever_married":ever_married,"work_type":work_type,"Residence_type":Residence_type,
        "avg_glucose_level":avg_glucose_level,"bmi":bmi,"smoking_status":smoking_status};

        $.ajax({
            url: 'main/api/make_prediction',
            data: inputData,
            type: 'post',
            success: function(response) {
                console.log(response);
                $('#hfProb').append(`<p style="color:white;">Patient has a ${response['pred']}% probability of a stroke</p>`)

                var figure = JSON.parse(response['plot']);
                Plotly.newPlot('hfPlot', figure.data, figure.layout, {
                    displayModeBar: false,
                    responsive: true
                });
            }
        })
    });

});