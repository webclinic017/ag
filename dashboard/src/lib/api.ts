type Param = {
    [key:string]: string | number
}

type ResponseProps<T> = {
    ack: boolean
    result: T
}



class API {
    constructor() {}

    private async fetch<T>(path:string, method: 'get' | 'post', params:Param[]): Promise<ResponseProps<T>> {
        return fetch(`http://localhost/${path}`, {
            method,
        }).then(r => {
            if(r.ok) {
                return r.json()
            }
            throw new Error('response error')
        }).then(json => 
            Promise.resolve(json)
        ).catch(err => {
            console.error(err)
            return Promise.reject(err)
        })
    }

    static async start() {
    }

    static async stop() {
    }

    static async pause() {
    }
}

export default API