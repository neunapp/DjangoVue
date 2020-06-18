new Vue({
  el: '#app',
  delimiters: ['{$', '$}'],
  data: {
    full_name: '',
    ocupation: '',
    age: 20,
    kword: '',
    lista_agregados: [],
    lista_lenguajes: []
  },
  watch: {
    kword: function (val) {
      this.BuscarLenguajes(val);
    }
  },
  methods: {
    BuscarLenguajes: function (kword) {
      var self = this;
      axios.get('/api/lenguaje/search/?kword=' + kword)
        .then(function (response) {
          self.lista_lenguajes = response.data
        })
        .catch( function (error) {
          console.log(error);
        })
    },
    AgregarLenguaje: function (lenguaje) {
      this.lista_agregados.push(lenguaje)
    },
    RegistrarProgramador: function () {
      //
      var lista_id_lenguajes = []
      for (let i = 0; i < this.lista_agregados.length; i++) {
        lista_id_lenguajes.push(this.lista_agregados[i].id)
      }
      //
      var data_programador = {
        'full_name': this.full_name,
        'ocupation': this.ocupation,
        'age': this.age,
        'languages': lista_id_lenguajes
      }

      axios.post('/api/programador/register/', data_programador)
        .then(function (response) {
          console.log(response)
        })
        .catch( function (error) {
          console.log(error);
        })
    }
  },
});