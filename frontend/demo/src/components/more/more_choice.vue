<template>
<div>
    <div class="rounded-3 shadow p-3 mb-5 bg-body rounded position-relative bodyset" @click="gotodownload($event)">
        <div class="insideset">
            <div class="picset">
                <img :src="send[8]" width="30px" height="30px" alt="1">
            </div>
            <div class="titleset">
                <div class="titleinsideset d-inline-block text-truncate" style="max-width: 150px;">
                    {{ send[1] }}
                </div>
                <div class="dateset" style="font-size:10px;">
                    最近更新于:{{ send[7] }}
                </div>
            </div>
        </div>
        <div class="contentset" style="font-size:10px;">
            {{ send[2] }}
        </div>
        <span class="position-relative position-absolute top-50 start-50 translate-middle badge bg-primary mouseset" @mouseleave="opac = 0" @mouseenter="opac = 0.8" :style="{ opacity: opac }">
            <svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="currentColor" class="bi bi-arrow-down-circle position-absolute top-50 start-50 translate-middle" viewBox="0 0 16 16">
                <path fill-rule="evenodd" d="M1 8a7 7 0 1 0 14 0A7 7 0 0 0 1 8zm15 0A8 8 0 1 1 0 8a8 8 0 0 1 16 0zM8.5 4.5a.5.5 0 0 0-1 0v5.793L5.354 8.146a.5.5 0 1 0-.708.708l3 3a.5.5 0 0 0 .708 0l3-3a.5.5 0 0 0-.708-.708L8.5 10.293V4.5z"/>
            </svg>    
        </span>
        <!-- 红色圆点 -->
        <!-- <span class="position-absolute top-0 start-100 translate-middle badge border bg-danger border-light rounded-circle p-2"><span class="visually-hidden"></span></span> -->
    </div>
</div>
</template>



<script>
import '@/assets/css/more_choice.css'


export default {
    props:['send'],
    name:'MoreChoice',
    data(){
        return{
            msg:'child',
            opac:0,
            link:'',
        }
    },
    mounted(){
        
    },
    methods:{
        gotodownload(event){
            var linknum = this.send[0];
            window.open(`http://81.68.105.198:70/#/click/${linknum}`);
        },
    },
}


</script>


<style>


</style>
