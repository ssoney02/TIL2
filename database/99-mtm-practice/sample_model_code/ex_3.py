from django.db import models


class Doctor(models.Model):
    # 환자 예약 조회하려면 역참조로 들어가야됨됨
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 의사 {self.name}'


class Patient(models.Model):
    # ManyToManyField 작성
    # doctors를 참조!
    doctors = models.ManyToManyField(Doctor)
    # 어차피 다대다 관계라서 ManyToManyField를 Doctor 모델쪽에 쓰든 Patient 모델쪽에 쓰든 상관없음
    # 대신!!!!! 참조와 역참조 관계가 바뀜
    # 물론 이름이 바뀔 순 있겠으나,, 테이블의 이름이 중요하진x..
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 환자 {self.name}'


# Reservation Class 주석 처리


# 코드 예시
doctor1 = Doctor.objects.create(name='allie')
patient1 = Patient.objects.create(name='carol')
patient2 = Patient.objects.create(name='duke')

# patient1이 새로 doctor에 대한 예약을 생성함
# add api?
patient1.doctors.add(doctor1)

patient1.doctors.all()
doctor1.patient_set.all()

doctor1.patient_set.add(patient2)
doctor1.patient_set.all()
patient2.doctors.all()
patient1.doctors.all()

doctor1.patient_set.remove(patient1)
doctor1.patient_set.all()
patient1.doctors.all()

patient2.patient_set.remove(doctor1)
patient2.doctors.all()
doctor1.patient_set.all()
