<template>
    <div class="d-flex justify-content-center">
        <div class="card" style="width: 17rem;">
        <img src="http://81.68.105.198:71/Rotation/gongju.jpg" class="card-img-top" style="height:170px;" alt="...">
        <div class="card-body">
            <h5 class="card-title">{{ send[1] }}</h5>
            <p class="card-text">{{ send[2] }}</p>
            <a @click="gotohots(send[0])" href="#" class="btn btn-primary">前往</a>
        </div>
        </div>
    </div>

</template>

<script>
export default {
    props:['send'],
    name:'DemoUsers',
    data(){
        return{

        }
    },
    methods:{
        gotohots:function(link){
            window.open(`http://81.68.105.198:70/#/click/${link}`)
        }
    }
}
</script>
