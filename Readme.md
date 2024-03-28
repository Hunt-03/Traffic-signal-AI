# Intel-Hackathon 
Team Name: Aim High Achieve High
Team Leader Email:2003sriraj@gmail.com
Enlightening Justice: Life threatening delays when traffic light becomes roadblocks to emergencies
Trained models


git lfs install
git clone https://github.com/Hunt-03/Traffic-signal-AI.git


# Problem Statement
In urban environments, the timely arrival of emergency services such as ambulances, fire trucks, and police vehicles can be critical in saving lives and preventing further damage. However, one significant obstacle that emergency responders often encounter is the delay caused by traffic lights, which can impede their rapid progress through intersections.

# Intel One API AIAnalytics toolkit- Boon for Developers ![image](https://github.com/Hunt-03/Traffic-signal-AI/tree/master/dataset)
This project aims to address this issue by developing an AI-based solution for effective traffic management and emergency vehicle prioritization. By integrating real-time video analysis, audio processing, and machine learning algorithms, the system will classify vehicles into normal and emergency categories based on size and the presence of siren sounds. Using these classifications, the system will dynamically adjust traffic signal timings to prioritize the passage of emergency vehicles while maintaining smooth traffic flow. Additionally, the system will consider factors such as vehicle count, time of day, and weather conditions to optimize signal timings. This comprehensive approach ensures timely emergency response and enhances overall traffic management efficiency.

# Description
We deployed the YOLO model,OpenCV library and techniques such as Deep Q Network along with certain adaptive control mechnisms on the *Intel CLoud Console* surpassing many larger models of its kind in terms of performance. Despite its enhanced capabilities, controlling its proclivity for hallucinations proved to be challenging. Extensive training was conducted using a substantial synthetic dataset gathered from diverse platforms, including large language model completion datasets, open-source information, and legal databases. This exhaustive training equipped the model with comprehensive knowledge of Indian laws, recent developments, significant judgments, and more.

# Intel AI analytics toolkit in Data preprocessing 
In bustling city settings, every second counts when it comes to emergency response. Picture this: ambulances, fire trucks, and police cars racing against time to reach those in need, their progress often hindered by the red light glow at intersections. This is where *Intel's AI analytics toolkit* steps in, like a silent hero behind the scenes. It's the engine that powers the behind-the-scenes magic, seamlessly weaving together a web of diverse data sources and churning out insights at lightning speed.

# Intel AI analytics toolkit in training
In the legal domain, the Intel AI analytics toolkit revolutionizes training by enhancing efficiency and effectiveness. Equipped with a foundational model enriched with Indian legal knowledge, we fine-tuned it for summarizing documents and generating content. Despite challenges with various models, we opted for a Zephyr 7B BETA quantized model in GPTQ format, leveraging Intel optimized PyTorch for code optimization. Despite setbacks like a system crash, our approach showed success with reduced training loss. With step-by-step guidance, Intel AI analytics toolkit proves invaluable in transforming legal support.

# Post training Quantization ![image](https://github.com/Hunt-03/Traffic-signal-AI/tree/master/dataset)
In urban environments, ensuring the prompt arrival of emergency services like ambulances, fire trucks, and police vehicles is paramount for preserving lives and mitigating additional harm. Nevertheless, a notable challenge faced by emergency responders is the hindrance posed by traffic lights, which frequently delays their swift traversal through intersections. To address this issue, post-training quantization methods, such as those applied to the YOLO model and TensorFlow on the Intel Cloud Console, prove invaluable. By reducing the computational resources required for inference without compromising accuracy, these quantization techniques enhance the responsiveness of traffic management systems, thereby facilitating the seamless passage of emergency vehicles and ultimately improving emergency response times.

# Experiments:
Various models were explored for summarization and data generation using own dataset on Intel Coud Console.




https://github.com/Hunt-03/Traffic-signal-AI/assets/131003334/147e4dba-0e82-49c6-9192-9efff7e6180a




# Usecase of Intel Developer cloud
The Intel Developer Cloud proves to be an excellent platform, offering access to powerful CPUs and high-speed internet, thereby facilitating a remarkably swift process. This challenges the misconception that LLM training necessitates GPU usage. The experimentation phase demonstrated that faster inferencing and training are achievable with different models on this platform.

For our misfortune at last moment when we trained the model with actual data, it got disconnected, which made us not use it at present, and the codes and screenshots are attached and the model is trained on other platform as per suggestion of intel team.

![image](https://idcbetabatch.eglb.intel.com/hub/user-redirect/doc/tree/test.py)


# Final output
1.Smart Legal Companion

Our model is now proficient in addressing inquiries related to Indian law, referencing crucial legal judgments, and comprehending and elucidating the nuances inherent in various laws and acts. Notably, it achieves this with significantly reduced inference time, providing efficient and accurate responses. The notebook named Simple inferencing with LLM and simple RAG chatbot in training notebooks proved to be very helpful while performing these activities.

Thanks to Intel AI Anlytics toolkit, which have made the inferencing much easy and fast compared with that of befor .only few line change have improved performance manyfold. These small changes have improved the performance very well

2. Signal Switch Algorithm
 The signal switching algorithm deployed on the Intel Cloud Console, leveraging the YOLO model and TensorFlow, represents a sophisticated approach to traffic management. By harnessing the power of computer vision and deep learning, this system can accurately detect and analyze traffic conditions in real-time. Using YOLO for object detection allows the algorithm to swiftly identify various elements such as vehicles, pedestrians, and cyclists from the live camera feeds at intersections. TensorFlow then steps in to analyze this data, providing insights into traffic patterns, congestion levels, and overall traffic flow dynamics. With this information at hand, the algorithm dynamically adjusts the timing of traffic signals, optimizing them to alleviate congestion and improve traffic flow efficiency. This dynamic signal adjustment ensures that intersections respond adaptively to changing traffic conditions, ultimately contributing to smoother traffic management and enhanced safety on the roads.

3. Vehicle detection module
 In urban environments, timely emergency response is crucial, yet traffic light delays often impede the swift passage of ambulances, fire trucks, and police vehicles through intersections. To overcome this obstacle, we employ the YOLO method integrated with OpenCV for real-time object detection. By training the YOLO model on a specialized dataset and customizing its configuration, we optimize accuracy for identifying vehicles and prioritizing emergency vehicles. This tailored traffic management solution aims to minimize delays and enhance public safety in urban areas.

# Future scope

1.*Integration of Advanced AI Techniques*: Explore the incorporation of advanced AI algorithms, such as reinforcement learning or deep reinforcement learning, to continuously optimize traffic signal switching in real-time based on dynamic traffic conditions and emergency vehicle presence.

2.*Smart City Infrastructure Integration*: Collaborate with city authorities to integrate the traffic management solution with existing smart city infrastructure, including traffic cameras, sensors, and IoT devices, to enable more comprehensive data collection and analysis.

3.*Predictive Analytics for Traffic Flow*: Develop predictive analytics models to forecast traffic patterns and trends, allowing for proactive signal adjustments and preemptive routing of emergency vehicles to minimize response times.

4.*Adaptation to Evolving Traffic Dynamics*: Continuously evolve the system's algorithms and models to adapt to changing traffic dynamics, such as peak traffic hours, special events, or road closures, to ensure optimal traffic flow and emergency vehicle prioritization.

5.*Collaboration with Emergency Services*: Foster partnerships with emergency service providers to gather real-time data on emergency vehicle locations and routes, enabling the system to dynamically adjust traffic signals to expedite their passage.

# Learnings and Insight
1. *Utilization of YOLO Method for Real-time Object Detection*:
     -Integration of YOLO (You Only Look Once) method in conjunction with OpenCV to enable real-time object detection of vehicles at intersections.

2. *Customized Training Dataset*:
     -Creation of a specialized dataset tailored for training the YOLO model, comprising diverse samples of vehicles encountered in urban traffic scenarios, including ambulances, fire trucks, police vehicles, and regular vehicles.

3. *Custom Configuration for Model Optimization*:
     -Customization of the YOLO model's configuration parameters to optimize accuracy specifically for identifying emergency vehicles and prioritizing them over regular vehicles.4

4. *Integration with Tensorflow and Intel Cloud Console*:
     -Utilization of Tensorflow framework for model training and optimization, alongside deployment and management through the Intel Cloud Console, ensuring seamless integration and scalability.

5. *Real-time Learning and Insights*:
     -Implementation of real-time learning mechanisms to continuously update the model based on new data and insights gathered from traffic conditions and emergency response scenarios.

6. *Dynamic Signal Adjustment and Priority Routing*:
     -Implementation of dynamic signal adjustment algorithms to prioritize the passage of emergency vehicles through intersections, based on real-time detection and classification of vehicles.

7. *Data-driven Decision Making*:
     -Leveraging insights gathered from the deployed system to inform data-driven decision-making processes aimed at further optimizing traffic management strategies and enhancing emergency response efficiency.

8. *Continuous Monitoring and Evaluation*:
     -Establishment of monitoring mechanisms to continuously evaluate the performance of the system, identify areas for improvement, and iteratively refine the model and algorithms for enhanced effectiveness.

 # Future Application Enhancement for intel:
  - Recognizing the prospective benefits of integrating Intel's features in future iterations.
  - Envisaging heightened end-to-end application performance through the strategic application of recently acquired insights and technologies.

  - Currently, our trained models undergo quantization to the GPTQ format for optimized performance, requiring the use of GPUs. Looking ahead, there is a potential shift towards quantizing them to GGML or OV formats, facilitating efficient inferencing even with CPU resources, as an alternative to the     current methodology.

# Tech stack used:
---------------streamlit
---------------IDC Jupyter Notebook Intel AI analytic ToolKit
---------------Model T5 zephyr


# Conclusion:

In conclusion, "Enlightening Justice" not only showcases the transformative power of AI and the Intel OneAPI AI Analytics Toolkit in the legal domain but also highlights the resilience of the team in overcoming challenges. The successful creation of a Traffic management for emergency vehicle system underscores the project's positive impact on legal professionals. Despite setbacks, the project's adaptability and forward-thinking approach ensure a promising trajectory for future advancements, marking a significant step toward revolutionizing legal support through cutting-edge technology and innovative solutions.


# Quick Steps

Required installation



clone repository

 
https://github.com/Hunt-03/Traffic-signal-AI


# Application
Built using streamlit

 streamlit run demo.py 
set the path of demo.py from hackathon folder
