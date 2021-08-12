<template>
    <div>
        <div style="margin-top:10px;">
            <div class="card">
                <div class="card-body">
                    <h5 class="card-title">{{ send[1] }}</h5>
                    <h6 class="card-subtitle mb-2 text-muted">{{ send[4] }}</h6>
                    <p class="card-text">{{ send[2] }}</p>
                    <span @click="gotohots(send[0])" class="text-primary">前往</span>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    props:["send"],
    name:"DemoHots",
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