<template>
  <div>
    <input @keyup.enter="onInputKeyword" type="text" />
  </div>
</template>

<script>
export default {
  name: "TheSearchBar",
  methods: {
    onInputKeyword: function () {
      //console.log(event.target.value)
      this.$emit("input-change", event.target.value);
    },
  },
};
</script>

<style></style>
