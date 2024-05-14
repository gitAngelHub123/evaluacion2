document.addEventListener('DOMContentLoaded', function() {
    const monedaEL_one = document.getElementById('moneda-uno');
    const monedaEL_two = document.getElementById('moneda-dos');
    const cantidadEL_one = document.getElementById('cantidad-uno');
    const cantidadEL_two = document.getElementById('cantidad-dos');
    const cambioEL = document.getElementById('cambio');

    function calcularCambio() {
        const moneda_one = monedaEL_one.value;
        const moneda_two = monedaEL_two.value;
        const cantidad_one = parseFloat(cantidadEL_one.value);

        let tasaCambio;

        // Definir las tasas de cambio manualmente
        const tasas = {
            'USD': {
                'EUR': 0.85,
                'CLP': 800
            },
            'EUR': {
                'USD': 1.18,
                'CLP': 940
            },
            'CLP': {
                'USD': 0.00125,
                'EUR': 0.00106
            }
        };

        // Obtener la tasa de cambio
        tasaCambio = tasas[moneda_one][moneda_two];

        // Calcular la cantidad convertida
        const cantidadConvertida = cantidad_one * tasaCambio;

        // Mostrar el resultado
        cambioEL.innerText = `${cantidad_one} ${moneda_one} = ${cantidadConvertida.toFixed(2)} ${moneda_two}`;
    };

    // Llamar a la función al cargar la página y cuando cambien los valores
    document.getElementById('taza').addEventListener('click', calcularCambio);
    document.getElementById('cantidad-uno').addEventListener('input', calcularCambio);
    document.getElementById('moneda-dos').addEventListener('change', calcularCambio);
});


document.addEventListener("DOMContentLoaded", function() {
    // Selecciona el botón por su ID
    var boton = document.getElementById("miBotonRegistro");

    // Agrega un event listener para el evento 'click'
    boton.addEventListener("click", function() {
        // Muestra una alerta personalizada utilizando SweetAlert2
        Swal.fire({
            title: 'usuario creado',
            icon: 'success',
            confirmButtonText: 'Aceptar',
            backdrop: true
        });
    });
});


document.addEventListener("DOMContentLoaded", function() {
    // Selecciona el botón por su ID
    var boton = document.getElementById("miBotonIniciarsesion");

    // Agrega un event listener para el evento 'click'
    boton.addEventListener("click", function() {
        // Muestra una alerta personalizada utilizando SweetAlert2
        Swal.fire({
            title: 'usuario logeado',
            icon: 'success',
            confirmButtonText: 'Aceptar',
            backdrop: true
        });
    });
});

