<template>
    <header>
        <h1>{{ title }}</h1>
    </header>
</template>

<script>

export default{
    name: 'TitleHeader',
    props: {
        title: String,
    },
}
</script>

<style scoped>
    header{
        align-items   : center;
        margin-bottom : 20px;
    }
</style>