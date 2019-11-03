<template>
    <v-container fluid fill-height>
        <v-layout row wrap align-center justify-center class="pa-0">
            <v-card class="px-5 py-3 mx-50" width="500" max>
                <v-avatar class="mb-4"
                    size="60"
                >
                    <img src="../../assets/img/T_logo.svg" alt="alt">
                </v-avatar>
                <v-form ref="signUpForm" max-width="1000">
                    <v-text-field
                    color="primary"
                     v-model.trim="name" name="name" label="الاسم" :rules="nameRules" required>
                    </v-text-field>
                    <v-text-field v-model="email" name="email" label="الايميل" :rules="emailRules" required
                        autocomplete="username">
                    </v-text-field>
                    <v-text-field v-model="password1" name="password" type="password" label=" كلمه السر "
                        :rules="passwordRules" required autocomplete="new-password">
                    </v-text-field>
                    <v-text-field v-model="password2" name="password" type="password" label=" أعد كلمه السر"
                        :rules="passwordRules1" required autocomplete="new-password">
                    </v-text-field>
                    <v-btn round @click="signUp" color="primary" class=" btn-shadow white--text my-4 ">استمرار</v-btn>
                </v-form>
                <v-flex>
                    <p>لديك حساب بالفعل ؟
                        <v-btn flat small @click="redirectToLogIn">
                            <span class="primary--text font-weight-bold ">دخول </span>
                        </v-btn>
                    </p>
                </v-flex>
            </v-card>
        </v-layout>
        <snack-bar />
    </v-container>
    </div>
</template>

<script>
    import snackBar from '../../components/sharedComponents/snackbar.vue'
    export default {
        components: {
            snackBar
        },
        data() {
            return {
                name: '',
                email: '',
                password1: '',
                password2: '',
                errors: [],
                nameRules: [
                    v => !!v || 'قم بإدخال إسم المستخدم ',
                    v => (v && v.length >= 3) || ' أسم المستخدم على الاقل 10 أحرف',
                    v => (v && v.length <= 20) || 'أسم المستخدم طويل جدا',
                ],
                emailRules: [
                    v => !!v || ' يجب إدخال البريدالإلكترني',
                    v => /.+@.+\..+/.test(v) || 'يجب إدخال بريد إلكتروني صالح',
                ],
                passwordRules: [
                    v => !!v || 'قم بإدخال كلمه المرور',
                    v => (v && v.length >= 8) || 'كلمه المرور على الاقل 8 أحرف',
                ],
                passwordRules1: [
                    v => !!v || ' أعد إدخال كلمه المرور',
                    v => (v && v.length >= 8) || 'على الاقل 8 أحرف',
                ],
            }
        },
        methods: {
            signUp: function () {
                if (this.$refs.signUpForm.validate()) {
                    if (this.password1 === this.password2) {
                        const userInfo = {
                            name: this.name,
                            email: this.email,
                            password1: this.password1,
                            password2: this.password2
                        }
                        console.log("user from vuefile " + userInfo + userInfo.name + userInfo.email + userInfo
                            .password1 + userInfo.password2)
                        this.$store.dispatch('register', {
                                name: userInfo.name,
                                email: userInfo.email,
                                password1: userInfo.password1,
                                password2: userInfo.password2
                            }).then(() => {
                                this.$store.commit('updateSnackBar', {
                                    message: 'تم التسجيل بنجاح',
                                    color: 'success'
                                })
                                this.$router.push('profile/EditProfile')
                            })
                            .catch(err => {
                                let snackbar = {
                                    message: 'حدث خطأ ما ، حاول مره أخرى',
                                    color: 'error'
                                }
                                console.log(err)
                                this.$store.commit('updateSnackbar', snackbar)
                            })
                    } else {
                        this.$store.commit('updateSnackbar', {
                            message: 'كلمه السر غير متشابهه',
                            color: 'error'
                        })
                    }
                }
            },
            redirectToLogIn() {
                this.$router.push('signin')
            }
        }
    }
</script>
<style lang="scss" scoped>
    @import '../../styles/views/signup/SignUp';
</style>