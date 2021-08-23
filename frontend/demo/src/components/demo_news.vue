<template>
<div class="row" style="margin-top:10px;">
  <a href="#" class="rounded-3 col-md-12 list-group-item list-group-item-action" aria-current="true" @click="gotonews(send[0])" @mouseleave="isactive = false" @mouseenter="isactive = true" :class="{ active: isactive }">
    {{ send[1] }}
  </a>
</div>
    
 
</template>

<script>
export default {
  props:['send'],
  name:'DemoNews',
    data(){
        return{
          isactive:false,
        }
    },
    methods:{
      gotonews:function(link){
        window.open(`http://81.68.105.198:70/#/news/${link}`);
      }
    }
  }
</script>


