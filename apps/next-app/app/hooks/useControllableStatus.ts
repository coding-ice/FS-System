import { useState } from "react"

interface ControllableValueProps<T> {
  defaultValue:T
  value?: T
  onChange?: (value: T) => void
}

function useControllableValue<T>({defaultValue, value, onChange}: ControllableValueProps<T>) {
  const [innerValue, setInnerValue] = useState(defaultValue)
  const mergedvalue = value ?? innerValue

  const set = (v: T) => {
    if(value === undefined) {
      setInnerValue(v)
    }
    onChange?.(v)
  }

  return [mergedvalue, set] as const
}

export default useControllableValue