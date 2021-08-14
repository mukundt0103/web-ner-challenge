<template>
    <div v-if="flag != 0" key="button-clicked">
        <!-- show no entities found is results is empty -->
        <div v-if="results.length < 1" key="no-entity">
            <b-container>
                <b-row class="justify-content-md-center">
                    <b-col col lg="6">
                        <b-alert show variant="danger">
                        No entities found
                        </b-alert>
                    </b-col>
                </b-row>
            </b-container>   
        </div>

        <div v-else>
            <b-container >
                <b-row align-v="stretch">
                    <!-- create column for each label -->
                    <b-col :key="result.label" v-for="result in results">
                        <b>{{ result.label }}</b> 
                        <hr style="border: none; border-bottom: 3px solid black;"/>
                        <!-- display text for this label -->
                        <div :key="text" v-for="text in result.text">
                        {{ text }}
                        <hr />
                        </div>
                    </b-col>
                </b-row>
            </b-container>
        </div>
    </div>
       
</template>

<script>
export default{
    name: 'NerResult',
    props: {
        results : Array,
        flag    : Number
    },
}    
</script>

<style scoped>
.result{
    display         : flex;
    justify-content : space-around;
}
</style>