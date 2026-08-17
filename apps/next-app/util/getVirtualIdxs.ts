export const getVirtualIdxs = (containerHeight: number, itemHeight: number, listLength: number, scrollTop: number, overscan: number = 5) => {
  const visableCount = Math.ceil(containerHeight / itemHeight)
  const startIdx = Math.max(0, Math.floor(scrollTop /itemHeight) - overscan)
  const endIdx = Math.min(listLength, startIdx + visableCount + 2 * overscan)

  return {
    startIdx,
    endIdx,
  }
}