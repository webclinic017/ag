import { createContext, Dispatch, FC, Reducer, useReducer } from "react";

export enum Bot_Status {
    ON  = "on",
    OFF = "off",
    PAUSED = "pause"
}

interface AppProps {
    status: Bot_Status
}

type ActionProps = {
    type: string
    payload: any
}

const initial_state = {
    status: Bot_Status.OFF
}

const AppContext = createContext<{state: AppProps, dispatch:Dispatch<ActionProps>}>({
    state: initial_state,
    dispatch: () => null
})


export enum Actions_Types {
    STATUS_CHANGED = "status_changed"
}

const reducer:Reducer<AppProps, ActionProps> = (state=initial_state, action) => {
    switch (action.type) {
        case Actions_Types.STATUS_CHANGED:
            return {...state, status: action.payload}
        default:
            return {...state}
    }
}


const AppContextProvider:FC = ({children}) => {
    const [state, dispatch] = useReducer(reducer, initial_state)
    return (
        <AppContext.Provider value={{state, dispatch}}>
            {children}
        </AppContext.Provider>
    )
}

export {
    AppContext,
    AppContextProvider
}
