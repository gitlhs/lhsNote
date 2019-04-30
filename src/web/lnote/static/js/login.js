            $(document).ready(function() {          
                $('#loginForm,#registForm').bootstrapValidator({
            //        live: 'disabled',
                    message: '该值无效',
                    feedbackIcons: {
                        valid: 'glyphicon glyphicon-ok',
                        invalid: 'glyphicon glyphicon-remove',
                        validating: 'glyphicon glyphicon-refresh'
                    },
                    fields: {
                        email: {
                            validators: {
                                emailAddress: {
                                    message: '不是一个合法的邮箱账号'
                                },
                                notEmpty: {
                                    message: 'email不能为空'
                                },
                            }
                        },
                        code: {
                            validators: {
                                notEmpty: {
                                    message: '验证码不能为空'
                                },
                            }
                        },

                        password: {
                            validators: {
                                notEmpty: {
                                    message: '密码不能为空'
                                },
                                stringLength: {
                                    min: 6,
                                    max: 16,
                                    message: '密码长度必须大于6个字符，小于16个字符'
                                },
                                regexp: {
                                    regexp: /^[a-zA-Z0-9_\.]+$/,
                                    message: '密码只能由字母、数字、点和下划线组成'
                                },
                                notEmpty: {
                                    message: '密码不能为空'
                                },
                                identical: {
                                    field: 'confirmPassword',
                                    message: '密码两次输入不一致'
                                },
                                different: {
                                    field: 'username',
                                    message: '密码不能和用户名一致'
                                }
                            }
                        },

                        confirmPassword: {
                            validators: {
                                notEmpty: {
                                    message: '确认密码是必需的，不能为空'
                                },
                                identical: {
                                    field: 'password',
                                    message: '两次密码输入不一致'
                                },
                                different: {
                                    field: 'username',
                                    message: '密码不能和用户名一致'
                                }
                            }
                        }
                    }
                });
            
                // 手动验证表单
                $('#validateBtn').click(function() {
                    $('#defaultForm').bootstrapValidator('validate');
                });
            
                $('#resetBtn').click(function() {
                    $('#defaultForm').data('bootstrapValidator').resetForm(true);
                });
            });
                //登录按钮js
                $('#button_login').on('click',function(e){
                    var url='/login_cgi';
                    var email = $('#exampleInputEmail1');
                    var password = $('#exampleInputPassword1');
                    var data = {
                        'email':email.val(),
                        'password':password.val()
                    };
                    $.post(url,data,function(json){
                        
                        
                        if(json.ret == 0){
                            window.location.href="/";
                        }else{
                            $('#login_alert').html("登录失败，请检查邮箱密码")
                        }
                    },'json')
                    // 后面加‘json‘指定json格式
                });