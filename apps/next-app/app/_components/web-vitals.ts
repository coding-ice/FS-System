"use client"
import {useReportWebVitals} from "next/web-vitals"

const WebVitals = () => {
  useReportWebVitals((metric) => {
    console.log(metric);
  });
};

export default WebVitals;