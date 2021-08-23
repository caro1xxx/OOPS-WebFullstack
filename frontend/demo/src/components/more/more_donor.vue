<template>
    <div>
        <div>
            <div class="card col-mb-3" style="margin-top:10px;">
                <div class="row g-0" @click="gotodownload($event)" @mouseleave="is = false" @mouseenter="is = true" :class="{ blue:is}">
                    <div class="col-md-4 d-none d-lg-block d-flex justify-content-center" style="padding:10px 60px;">
                        <img :src="send[7]" height="100px" width="100px" class="img-fluid rounded-center" alt="图片加载失败">
                        
                    </div>
                <div class="col-md-8">
                    <div class="card-body">
                        <h5 class="card-title">{{ send[1] }}</h5>
                        <p class="card-text">{{ send[2] }}</p>
                        <p class="card-text"><small class="text-muted">{{ send[6] }}</small></p>
                    </div>
                </div>
            </div>
            </div>
        </div>
    </div>
</template>

<script>

export default {
    props:['send'],
    name:'MoreDonor',
    data(){
        return{
            is:false,
        }
    },
    methods:{
        gotodownload(event){
            var linknum = this.send[0];
            window.open(`http://81.68.105.198:70/#/click2/${linknum}`);
        },
    },
}
</script>

<style>
.blue{
    background-color: #0D6EFD;
    color: #FFFFFF;
}
</style>