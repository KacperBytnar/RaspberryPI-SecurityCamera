const baseUri = "https://securitycamerawebapi20221215134018.azurewebsites.net"

Vue.createApp({
    data() {
        return {
            pictures : [],
            filteredPictures : [],
            deleteId: 0,
            deleteMessage:"",
            error: null
        }
    },
    async created() {
        console.log("created method called")
        // this.helperGetPosts(baseUri)
    },
    methods: {
        getAllPictures() {
            this.helperGetPosts(baseUri)
        },
        async helperGetPosts(uri) {
            try {
                const response = await axios.get(uri)
                this.pictures = await response.data
                this.filteredPictures = this.pictures
                //this.filteredData = this.dataseries
            } catch (ex) {
                this.pictures = []
                this.error = ex.message
            }
        },
        filterByDate(date) {
            console.log("Date: "+date)
            this.filteredPictures = this.pictures.filter(t => t.date.includes(date))
            console.log("Pictures: "+this.pictures)
        },
        filterByToday() {
            console.log("Filter today is active")
            this.filteredPictures = this.pictures.filter(t => t.date.includes(date.today()))
            console.log("Pictures: "+this.pictures)
        },
        async deleteButton(deleteId) {
            const url = baseUri + "/" + deleteId
            try {
                response = await axios.delete(url)
                this.deleteMessage = response.status + " " + response.statusText
                this.getAllPictures()
                
            } catch (ex) {
                alert(ex.message)
            }
        }
    }
}).mount("#app")