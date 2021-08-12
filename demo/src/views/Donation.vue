<template>
    <div class="donation" style="margin-top:90px;">
        <div class="container">
            <div class="row">
                <div class="col-md-8 offset-md-2">
                    <div class="shadow p-3 mb-5 bg-body rounded">
                        <div>
                            <img src="@/assets/OOPS.png" style="height:30px;" alt="">
                                <hr>
                                <div>
                                    <h4 class="fw-bold">请认真阅读</h4>
                                </div>
                                <div style="color:#6C757D" class="fw-light">
                                    <h6 class="fw-light">感谢您能捐赠本网站</h6>
                                    <h6 class="fw-light">由于运营网站有成本所以设立了捐赠这个功能，希望用户能理解</h6>
                                    <h6 class="fw-light">非强制捐赠，只是为了给捐赠了的用户表示感谢，会给予一些特殊权限，得到非捐赠者不能访问的页面资源</h6>
                                    <h6 class="fw-light">最后再次感谢您能使用本网站，我们竭诚为您服务</h6>
                                    <h6 class="fw-light">请捐赠支付成功了的用户记录好支付订单号，发送给客服，客服在24小时之内激活捐赠者权限</h6>
                                    <h6 class="fw-light">查看捐赠者权限是否激活成功，查看个人信息徽章会多出一个蓝色的</h6>
                                    <h5 class="fw-light">客服QQ:2667955243</h5>
                                </div>
                                <hr>
                                <div class="row">
                                    
                                    <div class="col-lg-2 offset-lg-10 col-md-4 offset-md-8 col-5 offset-8">
                                        -- OOPS运营
                                    </div>
                                    <div class="col-lg-2 col-md-3">
                                        <!-- Button trigger modal -->
                                        <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">
                                            支付
                                        </button>
                                        <!-- Modal -->
                                        <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
                                        <div class="modal-dialog modal-dialog-centered">
                                            <div class="modal-content">
                                            <div class="modal-header">
                                                <h5 class="modal-title" id="exampleModalLabel">微信</h5>
                                                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                                            </div>
                                            <div class="modal-body">
                                                <div class="row">
                                                    <div class="col-md-6">
                                                        <div style="height:30px" class="d-flex justify-content-center">
                                                            微信
                                                        </div>
                                                        <div class="d-flex justify-content-center">
                                                            <img width="150px;" height="150px;" src="@/assets/wechat.jpg" alt="">
                                                        </div>
                                                    </div>
                                                    <div class="col-md-6">
                                                        <div style="height:30px" class="d-flex justify-content-center">
                                                            支付宝
                                                        </div>
                                                        <div class="d-flex justify-content-center">
                                                            <img width="150px;" height="150px;" src="@/assets/alipay.jpg" alt="">
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                            <div class="modal-footer">
                                                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                                            </div>
                                            </div>
                                        </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name:"Donation",
    data(){
        return{

        }
    }
}
</script>