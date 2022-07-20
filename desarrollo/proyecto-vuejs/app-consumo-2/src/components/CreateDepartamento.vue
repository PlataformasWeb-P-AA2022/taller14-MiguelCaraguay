<template>
    <div class="pt-5">
        <form @submit.prevent="create" method="post">
            <div class="form-group">
                <label for="departamento">Costo del departamento</label>
                <input
                    type="number"
                    class="form-control"
                    id="departamento"
                    v-model="departamento.costo_departamento"
                    v-validate="'required'"
                    name="departamento"
                    placeholder="Ingrese costo departamento"
                    :class="{'is-invalid': errors.has('departamento.costo_departamento') && submitted}">
                <div class="invalid-feedback">
                    Please provide a valid costo del departamento.
                </div>
            </div>

            <div class="form-group">
                <label for="num_cuartos">Numero de cuartos</label>
                <input
                    type="number"
                    class="form-control"
                    id="num_cuartos"
                    v-model="departamento.num_cuartos"
                    v-validate="'required'"
                    name="num_cuartos"
                    placeholder="Ingrese Numero de cuartos"
                    :class="{'is-invalid': errors.has('departamento.num_cuartos') && submitted}">
                <div class="invalid-feedback">
                    Please provide a valid numero de cuartos.
                </div>
            </div>

            <div class="form-group">
                <label for="num_banios">Numero de Baños</label>
                <input
                    type="number"
                    class="form-control"
                    id="num_banios"
                    v-model="departamento.num_banios"
                    v-validate="'required'"
                    name="num_banios"
                    placeholder="Ingrese Numero de baños"
                    :class="{'is-invalid': errors.has('departamento.num_banios') && submitted}">
                <div class="invalid-feedback">
                    Please provide a valid numero de baños.
                </div>
            </div>

            <div class="form-group">
                <label for="valor_alicuota">Valor de Alicuota</label>
                <input
                    type="number"
                    class="form-control"
                    id="valor_alicuota"
                    v-model="departamento.valor_alicuota"
                    v-validate="'required'"
                    name="valor_alicuota"
                    placeholder="Ingrese Valor de Alicuota"
                    :class="{'is-invalid': errors.has('departamento.valor_alicuota') && submitted}">
                <div class="invalid-feedback">
                    Please provide a valid Valor de Alicuota.
                </div>
            </div>

            <div class="form-group">
              <br>
                <label for="propietario">Propietario</label>
                <select v-model="departamento.propietario">
                            <option v-for="e in propietariosList" :key="e.url" :value="e.url">{{ e.nombre }} {{ e.apellido }}</option>
                        </select>
            </div>
            <br>
            <button type="submit" class="btn btn-primary">Crear</button>
        </form>
    </div>
</template>

<script>

import axios from 'axios';

export default {
    data() {
        return {
            departamento: {
                costo_departamento: '',
                num_cuartos: '',
                num_banios: '',
                valor_alicuota: '',
            },
            propietariosList: [],
            submitted: false
        }
    },
    mounted() {
        this.getPropietariosList()
    },
    methods: {
      getPropietariosList() {
            axios
            .get('http://127.0.0.1:8000/api/propietarios/')
            .then(response => {
                this.propietariosList = response.data
            })
            .catch(error => {
                console.log(error)
            })

        },
        create: function (e) {
            this.$validator.validate().then(result => {
                this.submitted = true;
                if (!result) {
                    return;
                }
                axios.post('http://127.0.0.1:8000/api/departamentos/',
                        this.departamento
                    )
                    .then(response => {
                        this.$router.push('/departamentos');
                    })
            });
        }
    },
}
</script>
