<template>
  <div class="list-group">
    <a @click="gotohots(send[0])" href="#" class="list-group-item list-group-item-action" aria-current="true" style="margin-bottom:5px;" @mouseleave="isactive = false" @mouseenter="isactive = true" :class="{ active: isactive }">
      <div class="d-flex w-100 justify-content-between">
        <h5 class="mb-1">{{ send[1] }}</h5>
        <small>{{ send[4] }}</small>
      </div>
      <p class="mb-1">{{ send[2] }}</p>
      <small>相关信息:{{ send[3] }}</small>
    </a>
  </div>
</template>

<script>
export default {
    props:['send'],
    name:'DemoMains',
    data(){
        return{
          isactive:false,
        }
    },
    methods:{
        gotohots:function(link){
            window.open(`http://81.68.105.198:70/#/click/${link}`)
        }
    }
}
</script>