flowchart TD
    A[User Enters Platform] --> B{User Type?}
    B -->|Job Seeker| C[Create/Update Profile]
    B -->|Employer| D[Post Job/Internship]
    
    C --> E[Explore Opportunities]
    E --> F[Search Jobs]
    E --> G[Find Internships]
    E --> H[Access Resources]
    
    F --> I[AI-Powered Job Matching]
    G --> I
    I --> J[Apply for Positions]
    
    H --> K[Career Counseling]
    H --> L[Resume Building]
    H --> M[Interview Preparation]
    H --> N[Mentorship Programs]
    
    J --> O{Application Status}
    O -->|Accepted| P[Interview Process]
    O -->|Rejected| Q[Receive Feedback]
    
    D --> R[Review Applications]
    R --> S[Schedule Interviews]
    S --> T[Hire Candidates]
    
    P --> T
    T --> U[Successful Placement]
    
    style A fill:#f9d71c,stroke:#333,stroke-width:2px
    style U fill:#66c2a5,stroke:#333,stroke-width:2px
    style B fill:#8da0cb,stroke:#333,stroke-width:2px
    style I fill:#fc8d62,stroke:#333,stroke-width:2px
    style H fill:#e78ac3,stroke:#333,stroke-width:2px
