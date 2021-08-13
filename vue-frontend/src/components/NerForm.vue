<template>
  <b-form @submit="onSubmit" class="form">
    <div>
      <h4>Select Language</h4>
      <b-form-select v-model="language" :options="options"></b-form-select>
    </div>

    <div>
      <b-form-textarea
        id="input-1"
        v-model="text"
        rows="10"
        placeholder="Enter text"
        required
      ></b-form-textarea>
    </div>

    <div>    
      <b-button type="submit" variant="primary" style="margin-right:20px;"
      >Submit</b-button>

      <b-button type="button" variant="danger" @click="clearText"
      >Clear</b-button>
    </div>

  </b-form>
</template>

<script>
import axios from "axios";

export default{
    name: 'NerForm',
    data() {
        return {
            text     : '',
            language : 'English',
            options  : [
              { value: 'English', text: 'English' },
              { value: 'Spanish', text: 'Spanish' },
              { value: 'French', text: 'French' },
              { value: 'German', text: 'German' }
            ]
        }
    },
    methods:{
        clearText(){
          this.text = '';
          this.$emit('clear-flag', 0)
        },

        fetchResults(payload){

            axios
            .post("http://localhost:8080/ner-submit", payload)
            .then((res) => {
              this.$emit('show-result', res.data)
            });    
        },

        onSubmit(e){
            e.preventDefault();

            const payload = {
              text     : this.text,
              language : this.language,
            };
            this.fetchResults(payload);           
        }
    }
}
</script>

<style scoped>
.form {
  display        : flex;
  flex-direction : column;
  margin         : 20px;
  padding        : 5px;
}
.form > div {
  flex       : 1 1 auto;
  text-align : center;
  margin     : 10px;
}
</style>